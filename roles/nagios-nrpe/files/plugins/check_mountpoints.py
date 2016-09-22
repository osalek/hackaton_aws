#!/usr/bin/python

import string
import sys

fstab_content=open('/etc/fstab','r')
mountlist = list()
i=0
exitstatus=1
mounted=False
mountstate='Mounts not OK'


for line in fstab_content:
 if '#' not in line and len(line) > 2 and 'nfs' in line:
        (fstabfs,fstabmountpt,fstabtype,fstaboptions,fstabdump,fstabpass)=line.strip().split()
        procmounts_content=open('/proc/mounts','r')
        for line in procmounts_content:
                ((procfs,procmountpt,proctype,procoptions,procdump,procpass))=line.strip().split()
                if (fstabtype == 'nfs' or fstabtype == 'nfs4') and (proctype == 'nfs' or proctype == 'nfs4'):
                        if fstabmountpt == procmountpt:
                                mounted=True
        procmounts_content.close()
        if mounted:
                exitstatus=0
                mountstate='Mounts OK'
        else:
                exitstatus=1
                mountstate="Mounts not OK"
                print mountstate
                sys.exit(exitstatus)
        mounted=False

print mountstate
sys.exit(exitstatus)
