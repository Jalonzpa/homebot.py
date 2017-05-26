#!/bin/bash
echo "This first part of the script will set up your CHIP Pro to be able to download and run the HomeBot script."

echo "This script will ask for your password."
sleep 2

#Updates operating system
echo "Updating OS..."
sleep 2
sudo apt-get update
sudo apt-get upgrade
echo "Done!"

#Installs Python
echo "Installing Python..."
sleep 2
sudo apt-get install python
echo "Done!"

#Installs the unnoficial CHIP_IO v5.5 package
echo "Installing CHIP_IO..."
sleep 2
curl -O https://github.com/xtacocorex/CHIP_IO/releases/download/v0.5.6/python-chip-io_0.5.6-1_armhf.deb
sudo dpkg -i python-chip-io_0.5.6-1_armhf.deb
echo "Done!"

#Installs Adafruit_Python_GPIO
echo "Installing Adafruit_Python_GPIO..."
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install

echo "CHIP_IO and Adafruit_Python_GPIO are both made by xtacocorex!"

#Starts HomeBot script
echo "Installing HomeBotOS..."
sleep 2
curl -o homebot.py https://raw.githubusercontent.com/Jalonzpa/homebot_code/master/homebot.py
chmod +x homebot.py
echo "Installed!"
echo "Booting HomeBot..."
python homebot.py
