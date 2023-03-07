import re
import subprocess

data = subprocess.check_output(['arp', '-a']).decode('utf-8')
# print(repr(data))
newdata = data.replace("\r", "").replace("\n", " ")
print(newdata)
# print(re.findall("dynamic", newdata))
print(re.findall(
    "([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s*([a-z0-9]{1,2}\-[a-z0-9]{1,2}\-[a-z0-9]{1,2}\-[a-z0-9]{1,2}\-[a-z0-9]{1,2}\-[a-z0-9]{1,2})\s*dynamic", newdata))
