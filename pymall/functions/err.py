# -*- coding: utf-8 -*-
def err(s,c):
    s=str(s)
    c=str(c)
    if s == 'err_0000':
        print('未知错误！！！')
    elif s == 'err_0001':
        print('未知的 "'+c+'" 命令！！！请检查您的输入。')
    else:
        return 'ERROR'
    print(c+':'+s)