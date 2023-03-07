import subprocess
import re

data = subprocess.check_output(
    ['ipconfig', '/all']).decode('utf-8')

newdata = data
print(repr(newdata))
print(re.findall(
    "WiFi.*(IPv4 Address).*:.*([0-9]{3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,4})", newdata, re.DOTALL))
print(re.findall(
    "WiFi.*\s*(IPv4).*:\s([0-9]{3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,4}).*Subnet.*([0-9]{3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,4}).*DefaultGateway.*:([0-9]{3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1})", newdata))
