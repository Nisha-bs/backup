import subprocess as sp
import re

output = sp.check_output("ipconfig").decode("utf-8").replace("\n", " ")
print(output)

print(re.findall("(Subnet Mask).*:\s(\d+\.\d+\.\d+\.\d+)\s+Default Gateway", output))
