#!/usr/bin/python

from os import system

#runs aptitude update
print "updating cache please wait"
system("apt update")

#asks to upgrade packages
update = raw_input("upgrade all packages?")

if ("y" in update):
	#upgrades packages
	print "upgrading packages please wait"
	system("apt upgrade -y")
	print "done"
	system("exit")
else:
	exit(0)

