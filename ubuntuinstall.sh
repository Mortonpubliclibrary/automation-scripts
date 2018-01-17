#!/bin/bash
#This is a little setup script to get debian/ubuntu set up for me
#from a fresh install, I'll throw it on git incase anyone else could find it
#usefull


echo "please enter your sudo password. \r\n" #gets your sudo password
read password  # sets it to $password
echo "thank you, this shoudln't take long"
cd /home/$USERNAME

#updates the cache, and upgrades everything to the newest version
echo "[*] updating literally everything I possibly can."
echo $password | sudo -S apt update && upgrade && dist-upgrade && full-upgrade

echo "[*] installing neofetch"
echo $password | sudo -S apt install neofetch #installs neofetch

#this next session sets up our .bashrc file
echo "[*] setting upd bashrc file"
echo "#to display systeminfo and graphic" >> /home/$USERNAME/.bashrc
echo neofetch >> /home/$USERNAME/.bashrc

echo "[*] installing those scripts you love so much."
echo $password | sudo -S apt install git # installs git
cd /home/$USERNAME/Documents
mkdir scripts && cd scripts
git clone https://github.com/Mortonpubliclibrary/automation-scripts.git
cd automation-scripts

#this installs all the scripts that you know and love
chmod +x update.py getpack.sh
echo $password | sudo -S cp update.py /bin/update
echo $password | sudo -S cp getpack.sh /bin/getpack
cd debinstall
chmod +x debinstall.#!/bin/sh
echo $password | sudo -S cp debinstall.sh /bin/debin

echo "Done!!!"
