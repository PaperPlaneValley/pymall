# -*- coding: utf-8 -*-
#PyMall:Python语言编写的Python代码商店
#PaperPlaneValley纸飞机谷工作室
import os
import getpass
import socket
import sys

sys.path.append(r'./functions')
import analysisip
import err

def cmdIn():
    who=str(getpass.getuser())
    pwd=str(os.getcwd())
    hn=str(socket.gethostname())
    op=str('PM ['+who+'@'+hn+': '+pwd+' ] >>>')
    ip=str(input(op))
    return ip

print('\n使用 help 或 h 来查看帮助\n')

ip = str()
hc = ip

while 1:
    hc = ip
    ip=str(cmdIn())
    ip = ip.strip(' ')
    if ip.startswith('$u') == True:
        analysisip.acmd(hc+ip.strip('$u'))
    else:
        op = str(analysisip.acmd(ip))
        if op == 'ok':
            pass
        else:
            err.err(op,ip)