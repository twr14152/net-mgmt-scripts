#!/usr/bin/python

from jsonrpclib import Server
from pprint import pprint
import getpass

# 
# I added these authentication commands so I wouldnt have to store passwords in the file. 
# I also think it makes one more deliberate in their application as well as may provide some safe guards 
# from inadvertantly kicking the script off 
# I think it would be useful in producation. In lab testing is kind sucks!!. 
# To work around entering passwords all the time 
# comment out the current variables UN, PW, EPW, add them as static variable assignments 
# UN = "user1" 
# PW = "password2" 
# EPW = "password3" 

UN = raw_input("Username : ")
PW = getpass.getpass("Password : ")
EPW = getpass.getpass("enable password: ")

device_list = []
#You will need to create a file device_list.txt that will have the host you want to access
file1 = open('device_list.txt', 'r')
for line in file1:
    host_ip = line.strip()
    if host_ip:
        device_list.append(host_ip)
file1.close()
print device_list

host_commands = [{ "cmd": "enable", "input": EPW}]

#You will need to create a file cli_commands.txt that will have the commands you want to run
file2 = open('cli_commands.txt', 'r')
for line in file2:
    cmds = line.strip()
    if cmds:
        host_commands.append(cmds)
file2.close()
print host_commands

for ip in device_list:
    switch = Server ("https://%s:%s@%s/command-api" % (UN, PW, ip))
    response = switch.runCmds( 1,host_commands, 'json')
    pprint(response)

