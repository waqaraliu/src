#!/bin/bash
echo "Installing !"
echo user = $USER
sudo apt update
echo "Done Updating !"
sudo apt install python3-pip
echo "Done installing pip !"
sudo pip3 install flask
sudo pip3 install keyboard
echo "Done installing flask !"
sudo chmod +x /home/pi/src/Installation/launcher.sh
echo "All Done!"
