#/usr/bin/python

from os import system
import sys

def refresh():
	print "updateing cache please wait..."
	system("apt update")
def list():
	system("apt list --upgradeable")
	listan = raw_input("Upgrade all packages? ")
	if "y" in listan:
		upgrade()

def upgrade():
	system("apt upgrade -y")

refresh()

if len(sys.argv) !=2:

        answer = raw_input("Upgrade all packages? ")

        if "y" in answer:
                upgrade()
        elif answer == "list":
                list()

elif "y" in sys.argv[1]:
	upgrade()
elif sys.argv[1] == "list":
	list()
elif len(sys.argv) !=2:

	answer = raw_input("Upgrade all packages? ")

	if "y" in answer:
		upgrade()
	elif answer == "list":
		list()
		listan = raw_input("Upgrade all packages? ")
		if "y" in listan:
			upgrade()
else:
	system("exit")

