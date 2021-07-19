# bme680monitor

sudo apt-get install python3-dev python3-pip -y
sudo apt-get update -y
reboot
sudo apt-get install apache2 -y
sudo apt-get install git -y
sudo pip3 install --upgrade setuptools
sudo pip3 install board busio
sudo pip3 install adafruit-circuitpython-bme680
mkdir ~/code
cd code
git clone https://github.com/williamolyolson/bme680monitor
