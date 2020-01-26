# -*- coding: utf-8 -*-
import os
import getpass
import socket
import sys
def pmShell(ip):
    ip=ip.strip('')
    if ip == 'exit':
        sys.exit(0)
    elif ip == 'quit':
        sys.exit(0)
    elif ip == 'q':
        sys.exit(0)
    else:
        print("无法理解的 '"+ip+"'")
def cmdIn():
    who=str(getpass.getuser())
    pwd=str(os.getcwd())
    hn=str(socket.gethostname())
    op=str('PM ['+who+'@'+hn+': '+pwd+' ] >>>')
    ip=str(input(op))
    return ip
def analysis(ip):
    ip=ip.strip(' ')
    if ip.startswith('os') == True:
        os.system(ip.strip('os '))
    else:
        pmShell(ip)
while 1:
    analysis(cmdIn())