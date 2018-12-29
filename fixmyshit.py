#!/usr/bin/python
# Made by Fullcontrol
CRED = '\033[91m'
CEND = '\033[0m'


BGREEN = '\033[32M'
BEND = '\033[0m'

GPINK = '\033[95M'
GEND = '\033[0m'

PKILL = '\033[91M'
PEND = '\033[0m'
import subprocess, time

def system(cmd):
  subprocess.call(cmd, shell=True)
echo ("\e[91mBIT-OT/23849")
print(CRED + "Fixing Killing Process Errors" + CEND)
file = open("/proc/sys/fs/file-max", "w")
file.write ("999999999999999999")
file.close()
time.sleep(1)
print(BGREEN + "1 Error Addressed and fixed" + BEND)
system ("sed -i 's/1024/9999999/g' /usr/include/bits/typesizes.h")
system ("ulimit -n 99999")
time.sleep(1)
print(BGREEN + "2 Error Addressed and fixed" + BEND)
time.sleep(0.5)
print(GPINK + "MADE BY FULLCONTROL" + GEND)
time.sleep(0.3)
print(PKILL + "My job is Finished!" + PEND)