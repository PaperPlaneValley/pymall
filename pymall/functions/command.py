# -*- coding: utf-8 -*-
import os
def runCmd(cmd):
    cmd = str(cmd)
    cmd = cmd.lstrip('os')
    os.system(cmd)