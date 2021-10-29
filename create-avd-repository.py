#!/usr/bin/env python3
import json
import yaml
import csv
from cookiecutter.main import cookiecutter
import os
import argparse


def read_yaml_file(filename, load_all=False):
    with open(filename, mode='r') as f:
        if not load_all:
            yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        else:
            # convert generator to list before returning
            yaml_data = list(yaml.load_all(f, Loader=yaml.FullLoader))
    return yaml_data


def read_csv_file(filename):
    with open(filename, mode='r') as csv_file:
        csv_row_dict_list = list()
        for row in csv.DictReader(csv_file):
            updated_row_dict = dict()
            for k, v in row.items():
                # remove potential spaces left and right
                k = k.strip()
                if v:
                    v = v.strip()
                updated_row_dict.update({k: v})
            csv_row_dict_list.append(updated_row_dict)

    return csv_row_dict_list


if __name__ == "__main__":

    # Get cookiecutter output_directory from CLI argument or default
    parser = argparse.ArgumentParser(
        prog="AVD Cookiecutter",
        description="This script will create AVD repository based on data proved in CSVs directory.")
    parser.add_argument(
        '-out', '--output_directory', default='./avd-cookiecutter-output',
        help='Directory to keep the AVD repository produced by cookiecutter'
    )
    args = parser.parse_args()
    cookiecutter_output_dir = args.output_directory

    # find cookiecutter templates location
    cookiecutter_template_directory = os.path.join(
        os.getcwd(), '.cookiecutters/avd-cookiecutter')

    cookiecutter_json = {
        # _jinja2_env_vars was added in attempt to fix whitespace control
        # doesn't work as expected, more testing required
        # but doesn't hurt either =), keeping it here for reference
        '_jinja2_env_vars': {'lstrip_blocks': True, 'trim_blocks': True},
        'csv': {
            # load inventory
            'inventory': read_csv_file('CSVs/inventory.csv'),
            # load cabling plan
            'cabling_plan': read_csv_file('CSVs/cabling_plan.csv'),
            # load server connections
            'server_list': read_csv_file('CSVs/servers.csv'),
            # load server port profiles
            'server_port_profiles': read_csv_file('CSVs/server_port_profiles.csv'),
            # load tenants and vrfs
            'tenants_vrfs': read_csv_file('CSVs/tenants_and_vrfs.csv'),
            # load vlans and svis
            'vlans_svis': read_csv_file('CSVs/vlans_and_svis.csv')
        }

    }

    # load general parameters and update cookiecutter.json
    cookiecutter_json.update({
        'general': read_yaml_file('CSVs/general_parameters.yml')
    })

    # shortening cookiecutter filenames to avoid windows path length limit
    cookiecutter_json.update({
        'repository_name': cookiecutter_json['general']['avd_repository_name'],
        'fabric_name': cookiecutter_json['general']['fabric_name'],
        'inventory_name': f"{cookiecutter_json['general']['avd_repository_name']}-inventory",
        'all_switches_group': cookiecutter_json['general']['avd_repository_name'].upper(),
        'server_group_name': f"{cookiecutter_json['general']['fabric_name']}_SERVERS",
        'tenants_group_name': f"{cookiecutter_json['general']['fabric_name']}_TENANTS"
    })

    # build fabric variables
    cookiecutter_json.update({
        'fabric': {
            'spine_list': list(),
            'l3leaf_list': list(),
            'pod_list': list()
        }
    })

    # calculate leaf and spine IDs
    spine_id = 1
    l3leaf_id = 1
    for a_switch in cookiecutter_json['csv']['inventory']:

        if a_switch['type'] == 'spine':
            a_spine = dict()
            # update spine dict with known parameters
            a_spine.update(a_switch)
            # set spine id and increment it
            a_spine.update({
                'id': spine_id
            })
            spine_id += 1

            cookiecutter_json['fabric']['spine_list'].append(a_spine)

    for a_switch in cookiecutter_json['csv']['inventory']:

        if a_switch['type'] == 'l3leaf':
            a_leaf = dict()
            # update leaf dict with known parameters
            a_leaf.update(a_switch)
            # set leaf id and increment it
            a_leaf.update({
                'id': l3leaf_id
            })
            l3leaf_id += 1

            # build leaf to spine connections
            spine_list = list()
            uplink_to_spine_interfaces = list()  # l3leaf uplinks to spines
            spine_interfaces = list()  # spine connections to l3leaf

            for a_link in cookiecutter_json['csv']['cabling_plan']:
                if a_link['local_switch'] == a_switch['hostname']:
                    for a_spine in cookiecutter_json['fabric']['spine_list']:
                        if a_link['remote_switch'] == a_spine['hostname']:
                            spine_list.append(a_spine['hostname'])
                            uplink_to_spine_interfaces.append(
                                a_link['local_interface'])
                            spine_interfaces.append(a_link['remote_interface'])
                if a_link['remote_switch'] == a_switch['hostname']:
                    for a_spine in cookiecutter_json['fabric']['spine_list']:
                        if a_link['local_switch'] == a_spine['hostname']:
                            spine_list.append(a_spine['hostname'])
                            uplink_to_spine_interfaces.append(
                                a_link['remote_interface'])
                            spine_interfaces.append(a_link['local_interface'])

            a_leaf.update({
                'spines': spine_list,
                'uplink_to_spine_interfaces': uplink_to_spine_interfaces,
                'spine_interfaces': spine_interfaces
            })

            cookiecutter_json['fabric']['l3leaf_list'].append(a_leaf)

    # build pods and MLAG connections
    pod_number = 0
    # l3leaf_list_copy = cookiecutter_json['fabric']['l3leaf_list'].copy()
    l3leaf_list_sorted_copy = sorted(
        cookiecutter_json['fabric']['l3leaf_list'], key=lambda leaf: leaf['id']
    )
    while l3leaf_list_sorted_copy:
        bgp_start_asn = int(
            cookiecutter_json['general']['leaf_as_range'].split('-')[0])
        bgp_end_asn = int(
            cookiecutter_json['general']['leaf_as_range'].split('-')[-1])
        bgp_asn_list = list(range(bgp_start_asn, bgp_end_asn))
        a_pod = {
            'name': f'pod{pod_number}',
            'asn': bgp_asn_list[pod_number],
            'leafs': list()
        }
        pod_number += 1  # increment for next cycle
        a_leaf = l3leaf_list_sorted_copy.pop(0)
        peer_leaf = dict()  # init peer_leaf dict
        a_leaf_mlag_interfaces = list()  # list of mlag ports on the local switch
        peer_leaf_mlag_interfaces = list()  # list of mlag ports on the peer switch

        for a_link in cookiecutter_json['csv']['cabling_plan']:
            if a_link['local_switch'] == a_leaf['hostname']:
                for index, another_leaf in enumerate(l3leaf_list_sorted_copy):
                    if a_link['remote_switch'] == another_leaf['hostname']:
                        a_leaf_mlag_interfaces.append(
                            a_link['local_interface'])
                        peer_leaf_mlag_interfaces.append(
                            a_link['remote_interface'])
                        peer_leaf = l3leaf_list_sorted_copy.pop(index)

            elif a_link['remote_switch'] == a_leaf['hostname']:
                for index, another_leaf in enumerate(l3leaf_list_sorted_copy):
                    if a_link['local_switch'] == another_leaf['hostname']:
                        a_leaf_mlag_interfaces.append(
                            a_link['remote_interface'])
                        peer_leaf_mlag_interfaces.append(
                            a_link['local_interface'])
                        peer_leaf = l3leaf_list_sorted_copy.pop(index)

        a_leaf.update({
            'mlag_interfaces': a_leaf_mlag_interfaces
        })
        if peer_leaf:
            peer_leaf.update({
                'mlag_interfaces': peer_leaf_mlag_interfaces
            })
            a_pod.update({
                'leafs': [a_leaf, peer_leaf]
            })
        else:
            a_pod.update({
                'leafs': [a_leaf]
            })

        cookiecutter_json['fabric']['pod_list'].append(a_pod)

    # build servers and tenants
    cookiecutter_json.update({
        'services': {
            'servers': list(),
            'tenants': list()
        }
    })

    # build server data
    server_name_list = [server['server_name']
                        for server in cookiecutter_json['csv']['server_list']]
    for server_name in set(server_name_list):
        a_server = {
            'name': server_name,
            'switch_ports': list(),
            'switches': list(),
            'endpoint_ports': list()
        }
        for switchport in cookiecutter_json['csv']['server_list']:
            if switchport['server_name'] == server_name:
                if switchport['description']:
                    a_server.update({'description': switchport['description']})
                if switchport['rack_name']:
                    a_server.update({'rack': switchport['rack_name']})
                a_server['switches'].append(switchport['switch_hostname'])
                a_server['switch_ports'].append(switchport['switch_port'])
                if switchport['profile']:
                    a_server.update({'profile': switchport['profile']})
                if switchport['port_channel_mode']:
                    a_server.update({
                        'port_channel': {
                            'mode': switchport['port_channel_mode'],
                            'state': 'present'
                        }
                    })

        # add description to every connection
        for a_link in a_server['switch_ports']:
            a_server['endpoint_ports'].append(a_server['description'])

        cookiecutter_json['services']['servers'].append(a_server)

    # build tenant data
    tenant_name_list = [entry['tenant_name']
                        for entry in cookiecutter_json['csv']['tenants_vrfs']]
    for tenant_name in set(tenant_name_list):
        a_tenant = {
            'name': tenant_name,
            'vrfs': list(),
            'l2vlans': list()
        }
        # add IP VRFs
        for vrf_entry in cookiecutter_json['csv']['tenants_vrfs']:
            if vrf_entry['tenant_name'] == tenant_name:
                if vrf_entry['tenant_mac_vrf_base_vni']:
                    a_tenant.update(
                        {'mac_vrf_vni_base': vrf_entry['tenant_mac_vrf_base_vni']})
                vrf = {
                    'name': vrf_entry['ip_vrf_name'],
                    'vrf_vni': vrf_entry['ip_vrf_vni'],
                    'vtep_diagnostic': {
                        'loopback': vrf_entry['vrf_diagnostic_loopback_number'],
                        'loopback_ip_range': vrf_entry['vrf_diagnostic_loopback_ip_range']
                    }
                }
                # find svis in this vrf
                svi_list = list()
                for vlan_entry in cookiecutter_json['csv']['vlans_svis']:
                    if vlan_entry['tenant_name'] == tenant_name:
                        if vlan_entry['ip_vrf'] == vrf_entry['ip_vrf_name']:
                            svi_dict = {
                                'vlan_number': vlan_entry['vlan_number'],
                                'vlan_name': vlan_entry['vlan_name'],
                                'ip_address_virtual': vlan_entry['ip_virtual_address_and_mask']
                            }
                            if vlan_entry['filter_tags']:
                                svi_dict.update(
                                    {'tags': vlan_entry['filter_tags'].split()})
                            if vlan_entry['mtu']:
                                svi_dict.update(
                                    {'mtu': vlan_entry['mtu']})
                            if vlan_entry['igmp_snooping_enabled']:
                                svi_dict.update(
                                    {'igmp_snooping_enabled': vlan_entry['igmp_snooping_enabled']})
                            svi_list.append(svi_dict)
                if svi_list:
                    a_tenant.update({
                        'svis': svi_list
                    })
                a_tenant['vrfs'].append(vrf)

        # add L2-only VLANs
        l2_vlan_list = list()
        for vlan_entry in cookiecutter_json['csv']['vlans_svis']:
            if vlan_entry['tenant_name'] == tenant_name:
                if not vlan_entry['ip_vrf']:
                    vlan_dict = {
                        'vlan_number': vlan_entry['vlan_number'],
                        'vlan_name': vlan_entry['vlan_name'],
                    }
                    if vlan_entry['filter_tags']:
                        vlan_dict.update(
                            {'tags': vlan_entry['filter_tags'].split()})
                    l2_vlan_list.append(vlan_dict)
        if l2_vlan_list:
            a_tenant.update({
                'l2vlans': l2_vlan_list
            })

        cookiecutter_json['services']['tenants'].append(a_tenant)

    # write cookiecutter.json
    cookiecutter_json_filename = os.path.join(
        cookiecutter_template_directory, 'cookiecutter.json'
    )
    with open(cookiecutter_json_filename, 'w') as cc_json_file:
        json.dump(cookiecutter_json, cc_json_file, indent=4)

    # generate AVD project
    cookiecutter(cookiecutter_template_directory, no_input=True,
                 overwrite_if_exists=True, output_dir=cookiecutter_output_dir)
