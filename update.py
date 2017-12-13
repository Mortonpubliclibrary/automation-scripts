#/usr/bin/python
#this is meant to run on Debian based distros, or anything that uses apt to manage packages

from os import system
import sys

#how to use the program
usage = "python "sys.argv[0] "(list y)"

#refreshes the apt cache
def refresh():
	print "updateing cache please wait..."
	system("apt update")
#lists all upgradeable packages
def list():
	system("apt list --upgradeable")
	listan = raw_input("Upgrade all packages? ")
	if "y" in listan:
		upgrade()

#upgrades the system		
def upgrade():
	system("apt upgrade -y")

#refreshes the cache
refresh()

#checks to see if you gave it any instructions right off the bat
if len(sys.argv) !=2:

	#asks if you want to upgrade the packages
        answer = raw_input("Upgrade all packages? ")

	#checks to see if there is a y in your answer, if there is it upgrades
        if "y" in answer:
                upgrade()
        #checks to see if the answer you gave was "list" if it is then it lists upgradable programs
	elif answer == "list":
                list()

#checks to see if there you typed a y right after the name of the program, if so it upgrades with out asking
elif "y" in sys.argv[1]:
	upgrade()
#checks to see if you typed list after the name of the program, if so it lists upgradeable packages
elif sys.argv[1] == "list":
	list()

#tells you how to use the program
else:
	print usage

