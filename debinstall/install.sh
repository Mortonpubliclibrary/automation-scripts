#!/bin/bash
#run me to install debin
echo "#for debin" >> ~/.bashrc
echo "alias debin='debinstall.sh'
sudo apt isntall gdebi
sudo mv debinstall.sh /bin
sudo chmod +x /bin/debinstall.sh
