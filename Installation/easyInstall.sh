#!/bin/bash
echo "Installing !"
echo user = $USER
sudo apt update
echo "Done Updating !"
sudo apt install python3-pip
echo "Done installing pip !"
pip3 install flask
echo "Done installing flask !"
sudo chmod +x /home/pi/src/launcher.sh
echo "All Done!"