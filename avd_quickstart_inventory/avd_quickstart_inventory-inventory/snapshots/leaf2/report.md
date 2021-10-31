# leaf2 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
- [show running-config](#show-running-config)
- [show ip bgp summary](#show-ip-bgp-summary)
- [show bgp evpn summary](#show-bgp-evpn-summary)
## show bgp evpn summary

```
BGP summary information for VRF default
Router identifier 192.0.255.130, local AS number 65101
Neighbor Status Codes: m - Under maintenance
  Description              Neighbor         V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  spine1                   192.0.255.1      4 65001           2105      2114    0    0    1d05h Estab   12     12
  spine2                   192.0.255.2      4 65001           2108      2106    0    0    1d05h Estab   12     12
```
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 P2P_LINK_TO_SPINE1_Ethernet2
Et2                            up             up                 P2P_LINK_TO_SPINE2_Ethernet2
Et3                            up             up                 MLAG_PEER_leaf1_Ethernet3
Et4                            up             up                 
Et5                            up             up                 host1_leaf1_to_host1
Lo0                            up             up                 EVPN_Overlay_Peering
Lo1                            up             up                 VTEP_VXLAN_Tunnel_Source
Lo100                          up             up                 Tenant_A_OP_Zone_VTEP_DIAGNOSTICS
Ma0                            up             up                 oob_management
Po3                            up             up                 MLAG_PEER_leaf1_Po3
Po5                            down           lowerlayerdown     host1_leaf1_to_host1
Vl110                          up             up                 Tenant_A_OP_Zone_1
Vl1197                         up             up                 
Vl3009                         up             up                 MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone
Vl4093                         up             up                 MLAG_PEER_L3_PEERING
Vl4094                         up             up                 MLAG_PEER
Vx1                            up             up                 leaf2_VTEP
```
## show ip bgp summary

```
BGP summary information for VRF default
Router identifier 192.0.255.130, local AS number 65101
Neighbor Status Codes: m - Under maintenance
  Description              Neighbor         V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  leaf1                    10.255.251.0     4 65101           2087      2083    0    0    1d05h Estab   7      7
  spine1_Ethernet2         172.31.255.4     4 65001           2068      2074    0    0    1d05h Estab   4      4
  spine2_Ethernet2         172.31.255.6     4 65001           2076      2090    0    0    1d05h Estab   4      4
```
## show ip interface brief

```
Address
Interface       IP Address            Status     Protocol         MTU   Owner  
--------------- --------------------- ---------- ------------ --------- -------
Ethernet1       172.31.255.5/31       up         up              1500          
Ethernet2       172.31.255.7/31       up         up              1500          
Loopback0       192.0.255.130/32      up         up             65535          
Loopback1       192.0.254.1/32        up         up             65535          
Loopback100     10.255.1.2/32         up         up             65535          
Management0     192.168.123.22/24     up         up              1500          
Vlan110         10.1.10.1/24          up         up              1500          
Vlan1197        unassigned            up         up              9164          
Vlan3009        10.255.251.1/31       up         up              1500          
Vlan4093        10.255.251.1/31       up         up              1500          
Vlan4094        10.255.252.1/31       up         up              1500
```
## show lldp neighbors

```
Last table change time   : 1 day, 5:27:03 ago
Number of table inserts  : 13
Number of table deletes  : 1
Number of table drops    : 0
Number of table age-outs : 1

Port          Neighbor Device ID       Neighbor Port ID    TTL
---------- ------------------------ ---------------------- ---
Et1           spine1.lab.net           Ethernet2           120
Et2           spine2.lab.net           Ethernet2           120
Et3           leaf1.lab.net            Ethernet3           120
Et4           leaf1.lab.net            Ethernet4           120
Et5           host1                    Ethernet2           120
Ma0           host1                    Management0         120
Ma0           spine2.lab.net           Management0         120
Ma0           leaf3.lab.net            Management0         120
Ma0           leaf4.lab.net            Management0         120
Ma0           leaf1.lab.net            Management0         120
Ma0           host2                    Management0         120
Ma0           spine1.lab.net           Management0         120
```
## show running-config

```
! Command: show running-config
! device: leaf2 (cEOSLab, EOS-4.27.0F-24305004.4270F (engineering build))
!
no aaa root
!
username ansible_local privilege 15 role network-admin secret sha512 $6$Dzu11L7yp9j3nCM9$FSptxMPyIL555OMO.ldnjDXgwZmrfMYwHSr0uznE5Qoqvd9a6UdjiFcJUhGLtvXVZR1r.A/iF5aAt50hf/EK4/
username cvpadmin privilege 15 role network-admin secret sha512 $6$aQjjIocu2Pxl0baz$.3hUsqFqET6CHtNoc2nKIrmwPY39NYBaG.l2dX1hmiUc46lWorrG7V25b5XeqwSCJnRs4pOe9teK1/5RK8mve/
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.122.241:9910 -cvauth=key,qwerty -cvvrf=MGMT -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
!
vlan internal order ascending range 1006 1199
!
transceiver qsfp default-mode 4x10G
!
service routing protocols model multi-agent
!
hostname leaf2
ip name-server vrf MGMT 8.8.8.8
dns domain lab.net
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
spanning-tree mst 0 priority 4096
!
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 160
   name Tenant_A_VMOTION
!
vlan 3009
   name MLAG_iBGP_Tenant_A_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
!
vrf instance MGMT
!
vrf instance Tenant_A_OP_Zone
!
management api http-commands
   no shutdown
   !
   vrf MGMT
      no shutdown
!
management security
   password encryption-key common
!
interface Port-Channel3
   description MLAG_PEER_leaf1_Po3
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
!
interface Port-Channel5
   description host1_leaf1_to_host1
   switchport access vlan 110
   mlag 5
!
interface Ethernet1
   description P2P_LINK_TO_SPINE1_Ethernet2
   no switchport
   ip address 172.31.255.5/31
!
interface Ethernet2
   description P2P_LINK_TO_SPINE2_Ethernet2
   no switchport
   ip address 172.31.255.7/31
!
interface Ethernet3
   description MLAG_PEER_leaf1_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
!
interface Ethernet5
   description host1_leaf1_to_host1
   channel-group 5 mode active
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.0.255.130/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.0.254.1/32
!
interface Loopback100
   description Tenant_A_OP_Zone_VTEP_DIAGNOSTICS
   vrf Tenant_A_OP_Zone
   ip address 10.255.1.2/32
!
interface Management0
   description oob_management
   vrf MGMT
   ip address 192.168.123.22/24
!
interface Vlan110
   description Tenant_A_OP_Zone_1
   vrf Tenant_A_OP_Zone
   ip address virtual 10.1.10.1/24
!
interface Vlan3009
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone
   vrf Tenant_A_OP_Zone
   ip address 10.255.251.1/31
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   ip address 10.255.251.1/31
!
interface Vlan4094
   description MLAG_PEER
   no autostate
   ip address 10.255.252.1/31
!
interface Vxlan1
   description leaf2_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 160 vni 10160
   vxlan vrf Tenant_A_OP_Zone vni 10
!
ip virtual-router mac-address 00:1c:73:00:dc:01
ip address virtual source-nat vrf Tenant_A_OP_Zone address 10.255.1.2
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_A_OP_Zone
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.0.255.128/25 eq 32
   seq 20 permit 192.0.254.0/24 eq 32
!
mlag configuration
   domain-id pod0
   local-interface Vlan4094
   peer-address 10.255.252.0
   peer-link Port-Channel3
   reload-delay mlag 300
   reload-delay non-mlag 330
!
ip route vrf MGMT 0.0.0.0/0 192.168.123.1
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
!
router bgp 65101
   router-id 192.0.255.130
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 $1c$caHDPKDBzOjl6ZrDQLicDQ==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 $1c$caHDPKDBzOjl6ZrDQLicDQ==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65101
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 $1c$caHDPKDBzOjl6ZrDQLicDQ==
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor 10.255.251.0 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 10.255.251.0 description leaf1
   neighbor 172.31.255.4 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.4 remote-as 65001
   neighbor 172.31.255.4 description spine1_Ethernet2
   neighbor 172.31.255.6 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.6 remote-as 65001
   neighbor 172.31.255.6 description spine2_Ethernet2
   neighbor 192.0.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.0.255.1 remote-as 65001
   neighbor 192.0.255.1 description spine1
   neighbor 192.0.255.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.0.255.2 remote-as 65001
   neighbor 192.0.255.2 description spine2
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle Tenant_A_OP_Zone
      rd 192.0.255.130:10
      route-target both 10:10
      redistribute learned
      vlan 110
   !
   vlan-aware-bundle Tenant_A_VMOTION
      rd 192.0.255.130:10160
      route-target both 10160:10160
      redistribute learned
      vlan 160
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Tenant_A_OP_Zone
      rd 192.0.255.130:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 192.0.255.130
      neighbor 10.255.251.0 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
!
end
```
## show version

```
Arista cEOSLab
Hardware version: 
Serial number: 22B766F9E51D654AAD36AB9557DC3EB1
Hardware MAC address: 001c.733f.4b3b
System MAC address: 001c.733f.4b3b

Software image version: 4.27.0F-24305004.4270F (engineering build)
Architecture: i686
Internal build version: 4.27.0F-24305004.4270F
Internal build ID: fed9e33b-669e-42ea-bee6-c7bf3cca1a73
Image format version: 1.0

cEOS tools version: 1.1
Kernel version: 5.4.124+

Uptime: 1 day, 5 hours and 42 minutes
Total memory: 65574536 kB
Free memory: 34404596 kB
```
