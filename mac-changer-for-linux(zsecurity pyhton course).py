#!/usr/bin/env python

import subprocess

print("chose one of the interfaces below")
subprocess.call(["nmcli", "device", "status"])

interface = input("interfaces = ")
print("mac adress are written in xx:xx:xx:xx:xx:xx")
new_mac = input("new mac = ")

print("*changing mac address of " + interface + " to " + new_mac)

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


print("Mac address of interface " + interface + " are changed to " + new_mac)
print("to check the mac address, type 'ifconfig " + interface + "'")
