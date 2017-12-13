#!/bin/bash
usage = "debin (packagename) NOTE:packagename does not need to be complete but it does need to be the first part of the package"

gdebi /home/$USER/Downloads/$1*
