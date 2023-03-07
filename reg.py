# import os
# import subprocess
# import re
# # x = "Wdjfdf"
# x = os.system("ipconfig")
# print(type(x))
# n = re.search("W", x)
# print(n)
# # for i in x:
# #     print(i)
# import module
import subprocess
import re


dic = {}
# Traverse the ipconfig information
data = subprocess.check_output(
    ['ipconfig', '/all']).decode('utf-8')
data = data.replace("\n", "").replace("\r", "").replace(" ", "")
print(repr(data))
# Arrange the bytes data
# for item in data:

print(re.findall("WiFi.*IPv4Address\.*:(\d+\.\d+\.\d+\.\d+)", data))
# wifi = re.findall("WiFi.*", data)
# print(wifi)
# ipv = re.findall("IPv4", item)
# Default = re.findall("Default Gateway", item)
# Subnet = re.findall("Subnet Mask", item)

# # print(item.split('\r')[:-1])
# # print(ipv)
# if (ipv):
#     # print(item)
#     ip = re.findall("[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", item)
#     dic.update({ipv[0]: item})
# # if (wifi):
# #     dic.update({wifi[0]: ""})
# if (Default):
#     dic.update({Default[0]: item})
# if (Subnet):
#     dic.update({Subnet[0]: item})


# print(dic)
