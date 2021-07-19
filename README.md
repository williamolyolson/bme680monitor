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

sudo crontab -e

* * * * * /usr/bin/python3 /home/pi/code/bme680monitor/bme680.py
* * * * * (sleep 10 ; /usr/bin/python3 /home/pi/code/bme680monitor/bme680.py)
* * * * * (sleep 20 ; /usr/bin/python3 /home/pi/code/bme680monitor/bme680.py)
* * * * * (sleep 30 ; /usr/bin/python3 /home/pi/code/bme680monitor/bme680.py)
* * * * * (sleep 40 ; /usr/bin/python3 /home/pi/code/bme680monitor/bme680.py)
* * * * * (sleep 50 ; /usr/bin/python3 /home/pi/code/bme680monitor/bme680.py)
