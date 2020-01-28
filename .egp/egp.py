#-*- coding:UTF-8 -*-
#gitpush.py
#github.com/024026008/Python/gitpush
#work by 024026008
from os import system
from sys import exit
print('此程序用于进行git相关操作')
print('作者：024026008')
print('此程序为脚本版，在 仓库/.egp/ 中')
print('未经允许，严禁擅自修改发布！！！')
print('***如果程序报错，请用 ctrl + c 终止程序并重新执行***')
print('For Linux\n')
def bdts(lj):
    lj = str(lj)
    print('$ cd '+lj)
    system('cd '+lj)
    add=str(input('将要添加进仓库的文件。如果您想要添加整个目录，请输入“.” ：'))
    print('$ git add '+ add)
    system('git add '+add)
    while True:
        ip = str(input())
        if ip == 'q':
            break
        elif ip == 'd':
            ipa = str(input('$ git commit -m '))
            system('git commit -m '+ipa)
        else:
            commit=str(input('输入您对本次提交的注释：'))
            print('$ git commit -m "'+commit+'"')
            system('git commit -m "'+commit+'"')
    print('本地推送完成！\n')
def wlts(lj):
    lj = str(lj)
    print('$ cd '+lj)
    system('cd '+lj)
    url=str(input('远程仓库地址（要加 https:// 或 其他）：'))
    print('$ git remote add origin '+url)
    system('git remote add origin '+url)
    FenZhi=str(input('请输入要提交的分支（主分支是master）：'))
    print('$ git push -u origin '+FenZhi)
    system('git push -u origin '+FenZhi)
    print('网络推送完成！\n')
while True:
    if input() == 'q':
        exit(0)
    else:
        lj = str('..')
        bdts(lj)
        wlts(lj)