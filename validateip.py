import re
ip = "192.168.0.232"
x = re.match(
    r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])", ip)
print(x.group())
# ((25[0-5] | 2[0-4][0-9] | [01]?[0-9][0-9]?)\.){3}(25[0-5] | 2[0-4][0-9] | [01]?[0-9][0-9]?)
