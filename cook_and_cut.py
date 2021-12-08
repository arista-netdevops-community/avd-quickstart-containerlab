#!/usr/bin/env python3
import json
import yaml
import csv
from cookiecutter.main import cookiecutter
import os
import sys
import argparse
import re
import hashlib


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


# Class Cut loads input data from the files in specified directory
# This class may add some essential functions, but not application specific post-processing
class Cut:

    def __init__(self, data_input_directory) -> None:
        # init cookiecutter dict
        # in/out keys help to split processed and unprocessed data
        # and add another nesting level required for lists in cookiecutter.json to work
        self.cookiecutter_vars = {
            'in': dict(),  # unprocessed input data
            'out': dict(),  # processed output data
            # copy real jinja2 templates without rendering
            '_copy_without_render': [
                '*.j2'
            ]
        }
        # load all data from input directory and assign to corresponding dict keys
        data_input_directory_full_path = os.path.join(
            os.getcwd(), data_input_directory)
        if not os.path.isdir(data_input_directory_full_path):
            sys.exit(
                f'ERROR: Can not find data input directory {data_input_directory_full_path}')
        for a_name in os.listdir(data_input_directory_full_path):
            a_full_path = os.path.join(data_input_directory_full_path, a_name)
            if os.path.isfile(a_full_path):
                if '.csv' in a_name.lower():
                    list_of_dict_from_csv = read_csv_file(a_full_path)
                    self.cookiecutter_vars['in'].update({
                        # [:-4] removes .csv
                        a_name.lower()[:-4]: list_of_dict_from_csv
                    })
                elif '.yml' in a_name.lower():
                    data_from_yaml = read_yaml_file(a_full_path)
                    self.cookiecutter_vars['in'].update({
                        # [:-4] removes .yml
                        a_name.lower()[:-4]: data_from_yaml
                    })
                elif '.yaml' in a_name.lower():
                    data_from_yaml = read_yaml_file(a_full_path)
                    self.cookiecutter_vars['in'].update({
                        # [:-5] removes .yaml
                        a_name.lower()[:-5]: data_from_yaml
                    })

    def cut(self, cookiecutter_template_directory, cookiecutter_output_dir='.'):
        if not os.path.isdir(cookiecutter_template_directory):
            # if no fullpath specified, build fullpath from cwd
            cookiecutter_template_directory = os.path.join(
                os.getcwd(), cookiecutter_template_directory)
            if not os.path.isdir(cookiecutter_template_directory):
                # log error and exit if specifed template directory is not present in cwd
                sys.exit(
                    f'ERROR: cant find cookiecutter template directory {cookiecutter_template_directory}')
        # write cookiecutter.json
        cookiecutter_json_filename = os.path.join(
            cookiecutter_template_directory, 'cookiecutter.json')
        with open(cookiecutter_json_filename, 'w') as cc_json_file:
            json.dump(self.cookiecutter_vars, cc_json_file, indent=4)
        # run cookiecutter to build output data
        cookiecutter(cookiecutter_template_directory, no_input=True,
                     overwrite_if_exists=True, output_dir=cookiecutter_output_dir)


class Cook(Cut):

    def clab_links(self):
        # build links section for containerlab topology file
        self.cookiecutter_vars['out']['clab_links'] = list()
        # add inter-switch links from the cabling plan
        for a_link in self.cookiecutter_vars['in']['cabling_plan']:
            updated_local_int = 'eth'
            for link_name_segment in a_link['local_interface'].split('/'):
                updated_local_int += re.sub('[^0-9]',
                                            '', link_name_segment) + '_'
            updated_local_int = updated_local_int.rstrip('_')
            updated_remote_int = 'eth'
            for link_name_segment in a_link['remote_interface'].split('/'):
                updated_remote_int += re.sub('[^0-9]',
                                             '', link_name_segment) + '_'
            updated_remote_int = updated_remote_int.rstrip('_')
            self.cookiecutter_vars['out']['clab_links'].append({
                'local_switch': a_link['local_switch'],
                'local_interface': updated_local_int,
                'remote_switch': a_link['remote_switch'],
                'remote_interface': updated_remote_int
            })
        # sort servers by name
        server_list_sorted = sorted(
            self.cookiecutter_vars['in']['servers'], key=lambda server: server['server_name'])
        # add server ports
        server_name_count = dict()  # dict to count number of server name occurrences
        for a_server in server_list_sorted:
            if a_server['server_name'] not in server_name_count.keys():
                # if server name was not counted before, that is the first occurrence
                server_name_count.update({
                    a_server['server_name']: 1
                })
            else:
                # if server was already counted, increment the number
                server_name_count[a_server['server_name']] += 1
            updated_remote_int = 'eth'
            for link_name_segment in a_server['switch_port'].split('/'):
                updated_remote_int += re.sub('[^0-9]',
                                             '', link_name_segment) + '_'
            updated_remote_int = updated_remote_int.rstrip('_')
            self.cookiecutter_vars['out']['clab_links'].append({
                'local_switch': a_server['server_name'],
                # the interface on the server side will be auto named as eth1, eth2, etc.
                'local_interface': f'eth{server_name_count[a_server["server_name"]]}',
                'remote_switch': a_server['switch_hostname'],
                'remote_interface': updated_remote_int
            })

    def clab_mac_address(self):
        # convert switch system macs from original format to XXXX.XXXX.XXXX
        self.cookiecutter_vars['out']['clab_mac_address'] = list()
        for a_switch in self.cookiecutter_vars['in']['inventory']:
            mac_digits = re.sub('[^0-9a-fA-F]', '', a_switch['mac_address'])
            self.cookiecutter_vars['out']['clab_mac_address'].append({
                'hostname': a_switch['hostname'],
                'mac_address': f'{mac_digits[0:4]}.{mac_digits[4:8]}.{mac_digits[8:12]}'
            })

    def avd_spine_list(self):
        # build list of spines from the inventory and assign IDs
        self.cookiecutter_vars['out']['avd_spine_list'] = list()
        spine_list = [a_switch for a_switch in self.cookiecutter_vars['in']
                      ['inventory'] if a_switch['type'] == 'spine']
        for index, a_spine in enumerate(spine_list, start=1):
            a_spine.update({
                'id': index
            })
            self.cookiecutter_vars['out']['avd_spine_list'].append(a_spine)

    def avd_l3leaf_list(self):
        # build list of l3leafs from the inventory and assign IDs
        self.cookiecutter_vars['out']['avd_l3leaf_list'] = list()
        l3leaf_list = [a_switch for a_switch in self.cookiecutter_vars['in']
                       ['inventory'] if a_switch['type'] == 'l3leaf']
        for index, a_leaf in enumerate(l3leaf_list, start=1):
            a_leaf.update({
                'id': index
            })
            # build leaf to spine connections
            connected_spines = list()
            uplink_to_spine_interfaces = list()  # l3leaf uplinks to spines
            spine_interfaces = list()  # spine connections to l3leaf
            spine_list = [a_switch for a_switch in self.cookiecutter_vars['in']
                          ['inventory'] if a_switch['type'] == 'spine']
            for a_link in self.cookiecutter_vars['in']['cabling_plan']:
                if a_link['local_switch'] == a_leaf['hostname']:
                    for a_spine in spine_list:
                        if a_link['remote_switch'] == a_spine['hostname']:
                            connected_spines.append(a_spine['hostname'])
                            uplink_to_spine_interfaces.append(
                                a_link['local_interface'])
                            spine_interfaces.append(a_link['remote_interface'])
                if a_link['remote_switch'] == a_leaf['hostname']:
                    for a_spine in spine_list:
                        if a_link['local_switch'] == a_spine['hostname']:
                            connected_spines.append(a_spine['hostname'])
                            uplink_to_spine_interfaces.append(
                                a_link['remote_interface'])
                            spine_interfaces.append(a_link['local_interface'])

            a_leaf.update({
                'spines': connected_spines,
                'uplink_to_spine_list': uplink_to_spine_interfaces,
                'spine_interface_list': spine_interfaces
            })

            self.cookiecutter_vars['out']['avd_l3leaf_list'].append(a_leaf)

    def avd_l3leaf_pods(self):
        # build l3leafs pods: 2 switches per pod for MLAG, 1 switch per pod for EVPN AA
        self.cookiecutter_vars['out']['avd_l3leaf_pod_list'] = list()
        # run avd_l3leaf_list to be sure that l3leaf list with IDs is constructed first
        self.avd_l3leaf_list()
        # sort leafs by ID
        l3leaf_list_sorted = sorted(
            self.cookiecutter_vars['out']['avd_l3leaf_list'], key=lambda leaf: leaf['id'])
        # build leaf ASN pool
        bgp_start_asn = int(
            self.cookiecutter_vars['in']['avd_rs']['leaf_as_range'].split('-')[0])
        bgp_end_asn = int(
            self.cookiecutter_vars['in']['avd_rs']['leaf_as_range'].split('-')[-1])
        bgp_asn_list = list(range(bgp_start_asn, bgp_end_asn))

        # build pods as MLAG, active-active or standalone
        a_pod_number = 0
        while l3leaf_list_sorted:
            a_leaf = l3leaf_list_sorted.pop(0)
            a_pod = {
                'name': f'pod{a_pod_number}',
                'asn': bgp_asn_list[a_pod_number],
                'leafs': [a_leaf]
            }
            # check if there is an MLAG peer
            mlag_peer_leaf = dict()
            this_leaf_peer_link_ports = list()
            other_leaf_peer_link_ports = list()
            for a_link in self.cookiecutter_vars['in']['cabling_plan']:
                if 'MLAG' in a_link['notes_and_comments']:
                    mlag_peer_leaf_hostname = ''
                    if a_link['local_switch'] == a_leaf['hostname']:
                        mlag_peer_leaf_hostname = a_link['remote_switch']
                        this_leaf_peer_link_ports.append(a_link['local_interface'])
                        other_leaf_peer_link_ports.append(a_link['remote_interface'])
                    if a_link['remote_switch'] == a_leaf['hostname']:
                        mlag_peer_leaf_hostname = a_link['local_switch']
                        this_leaf_peer_link_ports.append(a_link['remote_interface'])
                        other_leaf_peer_link_ports.append(a_link['local_interface'])
                    if mlag_peer_leaf_hostname:
                        for other_leaf_index, other_leaf in enumerate(l3leaf_list_sorted):
                            if other_leaf['hostname'] == mlag_peer_leaf_hostname:
                                mlag_peer_leaf = l3leaf_list_sorted.pop(other_leaf_index)

            if this_leaf_peer_link_ports:
                a_leaf.update({
                    'mlag_interfaces': this_leaf_peer_link_ports
                })
            a_pod.update({
                'leafs': [a_leaf]
            })

            if mlag_peer_leaf:
                mlag_peer_leaf.update({
                    'mlag_interfaces': other_leaf_peer_link_ports
                })
                a_pod['leafs'].append(mlag_peer_leaf)

            # add filters if defined
            if 'node_filters' in self.cookiecutter_vars['in']:
                tenant_filters = list()
                tag_filters = list()
                always_include_vrfs_in_tenants = list()
                for a_node in self.cookiecutter_vars['in']['node_filters']:
                    for this_pod_leaf in a_pod['leafs']:
                        if a_node['hostname'] == this_pod_leaf['hostname']:
                            if 'filter_tenants' in a_node.keys():
                                tenant_filters += [a_filter.strip() for a_filter in a_node['filter_tenants'].split(',')]
                            if 'filter_tags' in a_node.keys():
                                tag_filters += [a_filter.strip() for a_filter in a_node['filter_tags'].split(',')]
                            if 'always_include_vrfs_in_tenants' in a_node.keys():
                                always_include_vrfs_in_tenants += [a_filter.strip() for a_filter in a_node['always_include_vrfs_in_tenants'].split(',')]

                if tenant_filters:
                    a_pod.update({
                        'filter_tenants': tenant_filters
                    })
                if tag_filters:
                    a_pod.update({
                        'filter_tags': tag_filters
                    })
                if always_include_vrfs_in_tenants:
                    a_pod.update({
                        'always_include_vrfs_in_tenants': always_include_vrfs_in_tenants
                    })

            # if pod name was specified expicitely
            for this_pod_leaf in a_pod['leafs']:
                if 'pod_name' in this_pod_leaf.keys():
                    if this_pod_leaf['pod_name']:
                        a_pod['name'] = this_pod_leaf['pod_name']

            if a_pod['name'] in [p['name'] for p in self.cookiecutter_vars['out']['avd_l3leaf_pod_list']]:
                sys.exit(f"ERROR: Pod name {a_pod['name']} already exists!")
            else:
                self.cookiecutter_vars['out']['avd_l3leaf_pod_list'].append(a_pod)

            a_pod_number += 1

    def avd_servers(self):
        # build AVD server variables
        self.cookiecutter_vars['out']['avd_servers'] = list()
        server_names = set(
            [server['server_name']
                for server in self.cookiecutter_vars['in']['servers']]
        )
        short_hashes_in_use = list()
        for a_server_name in sorted(server_names):
            a_server = {
                'server_name': a_server_name,
                'switch_ports': [srv['switch_port'] for srv in self.cookiecutter_vars['in']['servers'] if srv['server_name'] == a_server_name],
                'switches': [srv['switch_hostname'] for srv in self.cookiecutter_vars['in']['servers'] if srv['server_name'] == a_server_name],
                'description': [srv['description'] for srv in self.cookiecutter_vars['in']['servers'] if (
                    srv['server_name'] == a_server_name) and srv['description']][0],
                'rack_name': [srv['rack_name'] for srv in self.cookiecutter_vars['in']['servers'] if (
                    srv['server_name'] == a_server_name) and srv['rack_name']][0],
                'profile': [srv['profile'] for srv in self.cookiecutter_vars['in']['servers'] if (
                    srv['server_name'] == a_server_name) and srv['profile']][0],
                'port_channel_mode': [srv['port_channel_mode'] for srv in self.cookiecutter_vars['in']['servers'] if (
                    srv['server_name'] == a_server_name) and srv['port_channel_mode']][0]
            }
            is_not_mlag = True
            for switch_hostname in a_server['switches']:
                for a_pod in self.cookiecutter_vars['out']['avd_l3leaf_pod_list']:
                    for a_pod_leaf in a_pod['leafs']:
                        if a_pod_leaf['hostname'] == switch_hostname:
                            if 'mlag_interfaces' in a_pod_leaf.keys():
                                is_not_mlag = False

            # build short ESI for non-MLAG switches
            if is_not_mlag:
                
                id_string = a_server['server_name'] + ''.join(a_server['switch_ports']) + ''.join(
                    a_server['switches']) + a_server['rack_name']
                # get first 12 digits of the hash at a cost of increased collision
                short_hash = hashlib.sha256(
                    id_string.encode('utf-8')).hexdigest()[0:12]
                if short_hash in short_hashes_in_use:
                    sys.exit(f'ERROR: hash collision for server {a_server_name}')
                else:
                    short_hashes_in_use.append(short_hash)
                    a_server.update({
                        'short_esi': f'{short_hash[0:4]}:{short_hash[4:8]}:{short_hash[8:12]}'
                    })

            self.cookiecutter_vars['out']['avd_servers'].append(a_server)

    def avd_tenants(self):
        # build tenant and vrf data
        self.cookiecutter_vars['out']['tenants_vrfs'] = list()
        tenant_names = set([entry['tenant_name']
                           for entry in self.cookiecutter_vars['in']['tenants_vrfs']])
        for tenant_name in tenant_names:
            a_tenant = {
                'tenant_name': tenant_name,
                'vrfs': list(),
                'svis': list(),
                'l2vlans': list()
            }
            # add IP VRFs
            for entry in self.cookiecutter_vars['in']['tenants_vrfs']:
                if entry['tenant_name'] == tenant_name:
                    if entry['tenant_mac_vrf_base_vni']:
                        a_tenant.update(
                            {'mac_vrf_vni_base': entry['tenant_mac_vrf_base_vni']})
                    # remove redundant keys and add vrf data to the list
                    del entry['tenant_mac_vrf_base_vni']
                    a_tenant['vrfs'].append(entry)

            # add SVIs and L2 VLANs
            for entry in self.cookiecutter_vars['in']['vlans_and_svis']:
                is_a_l2_vlan = True  # by default set flag to count the VLAN as L2
                if entry['tenant_name'] == tenant_name:
                    if 'ip_vrf' in entry.keys():
                        if isinstance(entry['ip_vrf'], str):
                            if entry['ip_vrf'].strip():
                                # add an entry for a VLAN with SVI interface
                                svi = {
                                    'vlan_number': entry['vlan_number'],
                                    'vlan_name': entry['vlan_name'],
                                    'ip_vrf': entry['ip_vrf'],
                                    'ip_virtual_address_and_mask': entry['ip_virtual_address_and_mask'],
                                }
                                if 'mtu' in entry.keys():
                                    if entry['mtu']:
                                        if isinstance(entry['mtu'], str):
                                            if entry['mtu'].strip():
                                                svi.update(
                                                    {'mtu': entry['mtu']})
                                if 'igmp_snooping_enabled' in entry.keys():
                                    if isinstance(entry['igmp_snooping_enabled'], str):
                                        if entry['igmp_snooping_enabled'].strip():
                                            svi.update(
                                                {'igmp_snooping_enabled': entry['igmp_snooping_enabled']})
                                if 'filter_tags' in entry.keys():
                                    if isinstance(entry['filter_tags'], str):
                                        if entry['filter_tags'].strip():
                                            svi.update(
                                                {'filter_tags': [a_tag.strip() for a_tag in entry['filter_tags'].split(',')]})
                                a_tenant['svis'].append(svi)
                                is_a_l2_vlan = False  # change flag is VLAN has an SVI
                    if is_a_l2_vlan:
                        # add an entry for L2 only VLAN
                        l2_vlan = {
                            'vlan_number': entry['vlan_number'],
                            'vlan_name': entry['vlan_name']
                        }
                        if 'filter_tags' in entry.keys():
                            if isinstance(entry['filter_tags'], str):
                                if entry['filter_tags'].strip():
                                    l2_vlan.update(
                                        {'filter_tags': [a_tag.strip() for a_tag in entry['filter_tags'].split(',')]})
                        a_tenant['l2vlans'].append(l2_vlan)

            # add tenant entry
            self.cookiecutter_vars['out']['tenants_vrfs'].append(a_tenant)


if __name__ == "__main__":

    # Get cookiecutter output_directory from CLI argument or default
    parser = argparse.ArgumentParser(
        prog="Cook-and-cut",
        description="This script creates expanded data from cookiecutter templates.")
    parser.add_argument(
        '-in', '--input_directory', default='CSVs',
        help='Directory to keep the AVD repository produced by cookiecutter'
    )
    parser.add_argument(
        '-out', '--output_directory', default='.',
        help='Directory to keep the AVD repository produced by cookiecutter'
    )
    args = parser.parse_args()
    cc = Cook(args.input_directory)
    # create clab links
    cc.clab_links()
    cc.clab_mac_address()
    cc.avd_spine_list()
    cc.avd_l3leaf_list()
    cc.avd_l3leaf_pods()
    cc.avd_servers()
    cc.avd_tenants()
    cc.cut('.cookiecutters')
