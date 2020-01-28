# -*- coding: utf-8 -*-
import command
import q
import c

def acmd(ip):
    ip=ip.strip(' ')
    if ip == 'exit' or ip == 'quit' or ip == 'q':
        q.q()
        return 'ok'
    elif ip == 'c' or ip == 'clear':
        c.c()
        return 'ok'
    elif ip == '':
        return 'ok'
    elif ip.startswith('os') == True:
        command.runCmd(ip)
        return 'ok'

    else:
        return 'err_0001'