#!/usr/bin/python

import os

con = raw_input("are you on the Library's network and want to ssh into the server? ")

if "y" in con:
	os.system("ssh (administrator accoutn)@(server ip) -p (NONstandard ssh port we use)")
elif "n" in con:
	print "Ok, good bye."
else:
	print "Please answer yes or no. Exiting."
