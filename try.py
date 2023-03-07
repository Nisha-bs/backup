import re
out = [[{"zoneName": "Border_zone1"}, {"zoneName": "Border_zone_1"}]]

string = '''{"layer3VirtualNetworkType": "TENANT", "layer3VirtualNetworkName": "L3vn_1",
          "isDefaultRouteInjection": True,
          "routeLeak": {"isGlobalRouteLeakEnabled": True, "globalRouteLeak": {
              "globalToVrfPrefixList": ["10.1.1.1/16"]}, "isProviderRouteLeakEnabled": True, "providerRouteLeak": [{"providerVrfName": "VRF_Red"}]},
          "aggregatedRouteList": ["10.7.0.0/24", "10.7.1.1/24"],
          "prefixLimit": 2000,
          "targetBorderZones": [{"zoneName": "Border_zone_1"}, {"zoneName": "Border_zone1"}],
          "borderInterconnect": [
              {"borderDeviceManagementIpAddress": "10.194.54.155",
               "interfaceType": "L3_SUB_INTERFACE",
               "portName": "GigabitEthernet1/0/2.100", "vlanId": "200", "ipv4Address": "187.0.0.1",
                  "ipv4Mask": "24",
                  "ipv6Address": "2001:DB8:ABCD:12::1", "ipv6Mask": "64", "bgpPeering": {
                      "remoteIpv4Address": "187.0.0.2", "remoteIpv6Address": "2001:DB8:ABCD:12::2",
                      "remoteAutonomousSystemNumber": "1002"}, "isMulticastEnabled": True}]}'''

output = re.findall("targetBorderZones.*(\[.*\]),", string, re.DOTALL)
print(sorted(out))
