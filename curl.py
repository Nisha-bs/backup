import subprocess as sp
import re
# output = sp.getoutput("curl ifconfig.me/ip")
output = sp.getoutput("ipconfig")

print(output)
# print((output).replace("\n", ""))
