APPLICATION Name: Pi Remote Test Commit3

Note:

In order to install all linux dependencies, perform followinf steps

1- Go to /home/pi/src/Installation folder
2- Execute (sudo sh easyInstall.sh) or (sudo ./easyInstall.sh)

Above steps will install all packages needed by the service

Note:

To auto run Script on Startup, Either edit /etc/rc.local file or use crontab or any method to add the following line

sudo python3 /home/pi/src/main.py &
