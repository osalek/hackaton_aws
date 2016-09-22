#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess

cmd1 = "mongo admin --port 27017 --quiet --eval 'db.isMaster().ok'"
cmd2 = "mongo admin --port 27017 --quiet --eval 'db.isMaster().ismaster'"

ismaster1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
ismaster2 = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
out_ismaster1 = ismaster1.communicate()[0].split()
out_ismaster2 = ismaster2.communicate()[0].split()

if out_ismaster1[0] == "1" and out_ismaster2[0] == "true":
    msg = "OK Mongos connected to replica set"
    retcode = 0
else:
    msg = "Mongos can\'t connect to replica set"
    retcode = 2

print msg
sys.exit(retcode)
