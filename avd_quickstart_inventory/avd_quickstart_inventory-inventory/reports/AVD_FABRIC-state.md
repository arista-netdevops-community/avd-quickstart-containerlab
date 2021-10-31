
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 210 | 200 | 10 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| leaf1 |  37 | 35 | 2 | NTP, Interface State |
| leaf2 |  37 | 35 | 2 | NTP, Interface State |
| leaf3 |  37 | 35 | 2 | NTP, Interface State |
| leaf4 |  37 | 35 | 2 | NTP, Interface State |
| spine1 |  31 | 30 | 1 | NTP |
| spine2 |  31 | 30 | 1 | NTP |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  6 | 0 | 6 |
| Interface State |  66 | 62 | 4 |
| LLDP Topology |  20 | 20 | 0 |
| MLAG |  4 | 4 | 0 |
| IP Reachability |  16 | 16 | 0 |
| BGP |  42 | 42 | 0 |
| Routing Table |  32 | 32 | 0 |
| Loopback0 Reachability |  24 | 24 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | leaf1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 2 | leaf2 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 3 | leaf3 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 4 | leaf4 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 5 | spine1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 6 | spine2 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 32 | leaf1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - host1_leaf1_to_host1 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 34 | leaf2 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - host1_leaf1_to_host1 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 36 | leaf3 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - host2_leaf3_to_host2 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 38 | leaf4 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - host2_leaf3_to_host2 | FAIL | interface status: down - line protocol status: lowerLayerDown |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | leaf1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 2 | leaf2 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 3 | leaf3 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 4 | leaf4 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 5 | spine1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 6 | spine2 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 7 | leaf1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf2_Ethernet3 | PASS |  |
| 8 | leaf1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet1 | PASS |  |
| 9 | leaf1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet1 | PASS |  |
| 10 | leaf1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - host1_leaf1_to_host1 | PASS |  |
| 11 | leaf2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf1_Ethernet3 | PASS |  |
| 12 | leaf2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet2 | PASS |  |
| 13 | leaf2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet2 | PASS |  |
| 14 | leaf2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - host1_leaf1_to_host1 | PASS |  |
| 15 | leaf3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf4_Ethernet3 | PASS |  |
| 16 | leaf3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet3 | PASS |  |
| 17 | leaf3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet3 | PASS |  |
| 18 | leaf3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - host2_leaf3_to_host2 | PASS |  |
| 19 | leaf4 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf3_Ethernet3 | PASS |  |
| 20 | leaf4 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet4 | PASS |  |
| 21 | leaf4 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet4 | PASS |  |
| 22 | leaf4 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - host2_leaf3_to_host2 | PASS |  |
| 23 | spine1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_LEAF1_Ethernet1 | PASS |  |
| 24 | spine1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF2_Ethernet1 | PASS |  |
| 25 | spine1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF3_Ethernet1 | PASS |  |
| 26 | spine1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF4_Ethernet1 | PASS |  |
| 27 | spine2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_LEAF1_Ethernet2 | PASS |  |
| 28 | spine2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF2_Ethernet2 | PASS |  |
| 29 | spine2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF3_Ethernet2 | PASS |  |
| 30 | spine2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF4_Ethernet2 | PASS |  |
| 31 | leaf1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf2_Po3 | PASS |  |
| 32 | leaf1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - host1_leaf1_to_host1 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 33 | leaf2 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf1_Po3 | PASS |  |
| 34 | leaf2 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - host1_leaf1_to_host1 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 35 | leaf3 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf4_Po3 | PASS |  |
| 36 | leaf3 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - host2_leaf3_to_host2 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 37 | leaf4 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf3_Po3 | PASS |  |
| 38 | leaf4 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - host2_leaf3_to_host2 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 39 | leaf1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS |  |
| 40 | leaf1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS |  |
| 41 | leaf1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan110 - Tenant_A_OP_Zone_1 | PASS |  |
| 42 | leaf1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | PASS |  |
| 43 | leaf2 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS |  |
| 44 | leaf2 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS |  |
| 45 | leaf2 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan110 - Tenant_A_OP_Zone_1 | PASS |  |
| 46 | leaf2 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | PASS |  |
| 47 | leaf3 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS |  |
| 48 | leaf3 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS |  |
| 49 | leaf3 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan110 - Tenant_A_OP_Zone_1 | PASS |  |
| 50 | leaf3 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | PASS |  |
| 51 | leaf4 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS |  |
| 52 | leaf4 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS |  |
| 53 | leaf4 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan110 - Tenant_A_OP_Zone_1 | PASS |  |
| 54 | leaf4 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | PASS |  |
| 55 | leaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS |  |
| 56 | leaf2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS |  |
| 57 | leaf3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS |  |
| 58 | leaf4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS |  |
| 59 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 60 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS |  |
| 61 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | PASS |  |
| 62 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 63 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS |  |
| 64 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | PASS |  |
| 65 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 66 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS |  |
| 67 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | PASS |  |
| 68 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 69 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS |  |
| 70 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | PASS |  |
| 71 | spine1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 72 | spine2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 73 | leaf1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3 - remote: leaf2_Ethernet3 | PASS |  |
| 74 | leaf1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: spine1_Ethernet1 | PASS |  |
| 75 | leaf1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: spine2_Ethernet1 | PASS |  |
| 76 | leaf2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet3 | PASS |  |
| 77 | leaf2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: spine1_Ethernet2 | PASS |  |
| 78 | leaf2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: spine2_Ethernet2 | PASS |  |
| 79 | leaf3 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3 - remote: leaf4_Ethernet3 | PASS |  |
| 80 | leaf3 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: spine1_Ethernet3 | PASS |  |
| 81 | leaf3 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: spine2_Ethernet3 | PASS |  |
| 82 | leaf4 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3 - remote: leaf3_Ethernet3 | PASS |  |
| 83 | leaf4 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: spine1_Ethernet4 | PASS |  |
| 84 | leaf4 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: spine2_Ethernet4 | PASS |  |
| 85 | spine1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: leaf1_Ethernet1 | PASS |  |
| 86 | spine1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: leaf2_Ethernet1 | PASS |  |
| 87 | spine1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3 - remote: leaf3_Ethernet1 | PASS |  |
| 88 | spine1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet4 - remote: leaf4_Ethernet1 | PASS |  |
| 89 | spine2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: leaf1_Ethernet2 | PASS |  |
| 90 | spine2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: leaf2_Ethernet2 | PASS |  |
| 91 | spine2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3 - remote: leaf3_Ethernet2 | PASS |  |
| 92 | spine2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet4 - remote: leaf4_Ethernet2 | PASS |  |
| 93 | leaf1 | MLAG | MLAG State active & Status connected | MLAG | PASS |  |
| 94 | leaf2 | MLAG | MLAG State active & Status connected | MLAG | PASS |  |
| 95 | leaf3 | MLAG | MLAG State active & Status connected | MLAG | PASS |  |
| 96 | leaf4 | MLAG | MLAG State active & Status connected | MLAG | PASS |  |
| 97 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet1 - Destination: spine1_Ethernet1 | PASS |  |
| 98 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet2 - Destination: spine2_Ethernet1 | PASS |  |
| 99 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet1 - Destination: spine1_Ethernet2 | PASS |  |
| 100 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet2 - Destination: spine2_Ethernet2 | PASS |  |
| 101 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet1 - Destination: spine1_Ethernet3 | PASS |  |
| 102 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet2 - Destination: spine2_Ethernet3 | PASS |  |
| 103 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet1 - Destination: spine1_Ethernet4 | PASS |  |
| 104 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet2 - Destination: spine2_Ethernet4 | PASS |  |
| 105 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet1 - Destination: leaf1_Ethernet1 | PASS |  |
| 106 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet2 - Destination: leaf2_Ethernet1 | PASS |  |
| 107 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet3 - Destination: leaf3_Ethernet1 | PASS |  |
| 108 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet4 - Destination: leaf4_Ethernet1 | PASS |  |
| 109 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet1 - Destination: leaf1_Ethernet2 | PASS |  |
| 110 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet2 - Destination: leaf2_Ethernet2 | PASS |  |
| 111 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet3 - Destination: leaf3_Ethernet2 | PASS |  |
| 112 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet4 - Destination: leaf4_Ethernet2 | PASS |  |
| 113 | leaf1 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 114 | leaf2 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 115 | leaf3 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 116 | leaf4 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 117 | spine1 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 118 | spine2 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 119 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.1 | PASS |  |
| 120 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.0 | PASS |  |
| 121 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.2 | PASS |  |
| 122 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.0 | PASS |  |
| 123 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.4 | PASS |  |
| 124 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.6 | PASS |  |
| 125 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.5 | PASS |  |
| 126 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.8 | PASS |  |
| 127 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.10 | PASS |  |
| 128 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.4 | PASS |  |
| 129 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.12 | PASS |  |
| 130 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.14 | PASS |  |
| 131 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.1 | PASS |  |
| 132 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.5 | PASS |  |
| 133 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.9 | PASS |  |
| 134 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.13 | PASS |  |
| 135 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.3 | PASS |  |
| 136 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.7 | PASS |  |
| 137 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.11 | PASS |  |
| 138 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.15 | PASS |  |
| 139 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.1 | PASS |  |
| 140 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.2 | PASS |  |
| 141 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.1 | PASS |  |
| 142 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.2 | PASS |  |
| 143 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.1 | PASS |  |
| 144 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.2 | PASS |  |
| 145 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.1 | PASS |  |
| 146 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.2 | PASS |  |
| 147 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.129 | PASS |  |
| 148 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.130 | PASS |  |
| 149 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.131 | PASS |  |
| 150 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.132 | PASS |  |
| 151 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.129 | PASS |  |
| 152 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.130 | PASS |  |
| 153 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.131 | PASS |  |
| 154 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.132 | PASS |  |
| 155 | leaf1 | Routing Table | Remote Lo1 address | 192.0.254.1 | PASS |  |
| 156 | leaf1 | Routing Table | Remote Lo1 address | 192.0.254.3 | PASS |  |
| 157 | leaf2 | Routing Table | Remote Lo1 address | 192.0.254.1 | PASS |  |
| 158 | leaf2 | Routing Table | Remote Lo1 address | 192.0.254.3 | PASS |  |
| 159 | leaf3 | Routing Table | Remote Lo1 address | 192.0.254.1 | PASS |  |
| 160 | leaf3 | Routing Table | Remote Lo1 address | 192.0.254.3 | PASS |  |
| 161 | leaf4 | Routing Table | Remote Lo1 address | 192.0.254.1 | PASS |  |
| 162 | leaf4 | Routing Table | Remote Lo1 address | 192.0.254.3 | PASS |  |
| 163 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.129 | PASS |  |
| 164 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.130 | PASS |  |
| 165 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.131 | PASS |  |
| 166 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.132 | PASS |  |
| 167 | leaf2 | Routing Table | Remote Lo0 address | 192.0.255.129 | PASS |  |
| 168 | leaf2 | Routing Table | Remote Lo0 address | 192.0.255.130 | PASS |  |
| 169 | leaf2 | Routing Table | Remote Lo0 address | 192.0.255.131 | PASS |  |
| 170 | leaf2 | Routing Table | Remote Lo0 address | 192.0.255.132 | PASS |  |
| 171 | leaf3 | Routing Table | Remote Lo0 address | 192.0.255.129 | PASS |  |
| 172 | leaf3 | Routing Table | Remote Lo0 address | 192.0.255.130 | PASS |  |
| 173 | leaf3 | Routing Table | Remote Lo0 address | 192.0.255.131 | PASS |  |
| 174 | leaf3 | Routing Table | Remote Lo0 address | 192.0.255.132 | PASS |  |
| 175 | leaf4 | Routing Table | Remote Lo0 address | 192.0.255.129 | PASS |  |
| 176 | leaf4 | Routing Table | Remote Lo0 address | 192.0.255.130 | PASS |  |
| 177 | leaf4 | Routing Table | Remote Lo0 address | 192.0.255.131 | PASS |  |
| 178 | leaf4 | Routing Table | Remote Lo0 address | 192.0.255.132 | PASS |  |
| 179 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.129 | PASS |  |
| 180 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.130 | PASS |  |
| 181 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.131 | PASS |  |
| 182 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.132 | PASS |  |
| 183 | spine2 | Routing Table | Remote Lo0 address | 192.0.255.129 | PASS |  |
| 184 | spine2 | Routing Table | Remote Lo0 address | 192.0.255.130 | PASS |  |
| 185 | spine2 | Routing Table | Remote Lo0 address | 192.0.255.131 | PASS |  |
| 186 | spine2 | Routing Table | Remote Lo0 address | 192.0.255.132 | PASS |  |
| 187 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.129 | PASS |  |
| 188 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.130 | PASS |  |
| 189 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.131 | PASS |  |
| 190 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.132 | PASS |  |
| 191 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.0.255.130 Destination: 192.0.255.129 | PASS |  |
| 192 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.0.255.130 Destination: 192.0.255.130 | PASS |  |
| 193 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.0.255.130 Destination: 192.0.255.131 | PASS |  |
| 194 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.0.255.130 Destination: 192.0.255.132 | PASS |  |
| 195 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.0.255.131 Destination: 192.0.255.129 | PASS |  |
| 196 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.0.255.131 Destination: 192.0.255.130 | PASS |  |
| 197 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.0.255.131 Destination: 192.0.255.131 | PASS |  |
| 198 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.0.255.131 Destination: 192.0.255.132 | PASS |  |
| 199 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.0.255.132 Destination: 192.0.255.129 | PASS |  |
| 200 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.0.255.132 Destination: 192.0.255.130 | PASS |  |
| 201 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.0.255.132 Destination: 192.0.255.131 | PASS |  |
| 202 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.0.255.132 Destination: 192.0.255.132 | PASS |  |
| 203 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.129 | PASS |  |
| 204 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.130 | PASS |  |
| 205 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.131 | PASS |  |
| 206 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.132 | PASS |  |
| 207 | spine2 | Loopback0 Reachability | Loopback0 Reachability | Source: spine2 - 192.0.255.2 Destination: 192.0.255.129 | PASS |  |
| 208 | spine2 | Loopback0 Reachability | Loopback0 Reachability | Source: spine2 - 192.0.255.2 Destination: 192.0.255.130 | PASS |  |
| 209 | spine2 | Loopback0 Reachability | Loopback0 Reachability | Source: spine2 - 192.0.255.2 Destination: 192.0.255.131 | PASS |  |
| 210 | spine2 | Loopback0 Reachability | Loopback0 Reachability | Source: spine2 - 192.0.255.2 Destination: 192.0.255.132 | PASS |  |
