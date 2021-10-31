# spine1 Commands Output

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
Router identifier 192.0.255.1, local AS number 65001
Neighbor Status Codes: m - Under maintenance
  Description              Neighbor         V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  leaf1                    192.0.255.129    4 65101           2115      2107    0    0    1d05h Estab   6      6
  leaf2                    192.0.255.130    4 65101           2114      2105    0    0    1d05h Estab   6      6
  leaf3                    192.0.255.131    4 65102           2100      2098    0    0    1d05h Estab   6      6
  leaf4                    192.0.255.132    4 65102           2099      2113    0    0    1d05h Estab   6      6
```
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 P2P_LINK_TO_LEAF1_Ethernet1
Et2                            up             up                 P2P_LINK_TO_LEAF2_Ethernet1
Et3                            up             up                 P2P_LINK_TO_LEAF3_Ethernet1
Et4                            up             up                 P2P_LINK_TO_LEAF4_Ethernet1
Lo0                            up             up                 EVPN_Overlay_Peering
Ma0                            up             up                 oob_management
```
## show ip bgp summary

```
BGP summary information for VRF default
Router identifier 192.0.255.1, local AS number 65001
Neighbor Status Codes: m - Under maintenance
  Description              Neighbor         V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  leaf1_Ethernet1          172.31.255.1     4 65101           2079      2084    0    0    1d05h Estab   3      3
  leaf2_Ethernet1          172.31.255.5     4 65101           2074      2068    0    0    1d05h Estab   3      3
  leaf3_Ethernet1          172.31.255.9     4 65102           2081      2082    0    0    1d05h Estab   3      3
  leaf4_Ethernet1          172.31.255.13    4 65102           2084      2088    0    0    1d05h Estab   3      3
```
## show ip interface brief

```
Address
Interface       IP Address            Status     Protocol         MTU   Owner  
--------------- --------------------- ---------- ------------ --------- -------
Ethernet1       172.31.255.0/31       up         up              1500          
Ethernet2       172.31.255.4/31       up         up              1500          
Ethernet3       172.31.255.8/31       up         up              1500          
Ethernet4       172.31.255.12/31      up         up              1500          
Loopback0       192.0.255.1/32        up         up             65535          
Management0     192.168.123.11/24     up         up              1500
```
## show lldp neighbors

```
Last table change time   : 1 day, 5:27:05 ago
Number of table inserts  : 11
Number of table deletes  : 0
Number of table drops    : 0
Number of table age-outs : 0

Port          Neighbor Device ID       Neighbor Port ID    TTL
---------- ------------------------ ---------------------- ---
Et1           leaf1.lab.net            Ethernet1           120
Et2           leaf2.lab.net            Ethernet1           120
Et3           leaf3.lab.net            Ethernet1           120
Et4           leaf4.lab.net            Ethernet1           120
Ma0           host1                    Management0         120
Ma0           spine2.lab.net           Management0         120
Ma0           leaf3.lab.net            Management0         120
Ma0           leaf4.lab.net            Management0         120
Ma0           leaf1.lab.net            Management0         120
Ma0           leaf2.lab.net            Management0         120
Ma0           host2                    Management0         120
```
## show running-config

```
! Command: show running-config
! device: spine1 (cEOSLab, EOS-4.27.0F-24305004.4270F (engineering build))
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
hostname spine1
ip name-server vrf MGMT 8.8.8.8
dns domain lab.net
!
spanning-tree mode none
!
vrf instance MGMT
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
interface Ethernet1
   description P2P_LINK_TO_LEAF1_Ethernet1
   no switchport
   ip address 172.31.255.0/31
!
interface Ethernet2
   description P2P_LINK_TO_LEAF2_Ethernet1
   no switchport
   ip address 172.31.255.4/31
!
interface Ethernet3
   description P2P_LINK_TO_LEAF3_Ethernet1
   no switchport
   ip address 172.31.255.8/31
!
interface Ethernet4
   description P2P_LINK_TO_LEAF4_Ethernet1
   no switchport
   ip address 172.31.255.12/31
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.0.255.1/32
!
interface Management0
   description oob_management
   vrf MGMT
   ip address 192.168.123.11/24
!
ip routing
no ip routing vrf MGMT
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.0.255.0/25 eq 32
!
ip route vrf MGMT 0.0.0.0/0 192.168.123.1
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
router bgp 65001
   router-id 192.0.255.1
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
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
   neighbor 172.31.255.1 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.1 remote-as 65101
   neighbor 172.31.255.1 description leaf1_Ethernet1
   neighbor 172.31.255.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.5 remote-as 65101
   neighbor 172.31.255.5 description leaf2_Ethernet1
   neighbor 172.31.255.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.9 remote-as 65102
   neighbor 172.31.255.9 description leaf3_Ethernet1
   neighbor 172.31.255.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.13 remote-as 65102
   neighbor 172.31.255.13 description leaf4_Ethernet1
   neighbor 192.0.255.129 peer group EVPN-OVERLAY-PEERS
   neighbor 192.0.255.129 remote-as 65101
   neighbor 192.0.255.129 description leaf1
   neighbor 192.0.255.130 peer group EVPN-OVERLAY-PEERS
   neighbor 192.0.255.130 remote-as 65101
   neighbor 192.0.255.130 description leaf2
   neighbor 192.0.255.131 peer group EVPN-OVERLAY-PEERS
   neighbor 192.0.255.131 remote-as 65102
   neighbor 192.0.255.131 description leaf3
   neighbor 192.0.255.132 peer group EVPN-OVERLAY-PEERS
   neighbor 192.0.255.132 remote-as 65102
   neighbor 192.0.255.132 description leaf4
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
!
end
```
## show version

```
Arista cEOSLab
Hardware version: 
Serial number: AE1C5E586EA6ADC8EC22382484FE07AA
Hardware MAC address: 001c.7328.876f
System MAC address: 001c.7328.876f

Software image version: 4.27.0F-24305004.4270F (engineering build)
Architecture: i686
Internal build version: 4.27.0F-24305004.4270F
Internal build ID: fed9e33b-669e-42ea-bee6-c7bf3cca1a73
Image format version: 1.0

cEOS tools version: 1.1
Kernel version: 5.4.124+

Uptime: 1 day, 5 hours and 42 minutes
Total memory: 65574536 kB
Free memory: 34410424 kB
```
