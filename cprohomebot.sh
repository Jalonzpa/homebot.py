#!/bin/bash
echo "This first part of the script will set up your CHIP Pro to be able to download and run the HomeBot script."

echo "This script will ask for your password."

#Installs the set_antenna script
echo "Installing set_antenna script..."
curl -O https://raw.githubusercontent.com/NextThingCo/CHIP-buildroot/d4e5ddd02b5b5cb3ae37026b0743dcba1c724fc3/package/rtl8723ds_mp_driver/set_antenna
chmod +x set_antenna
sudo mv set_antenna /usr/sbin
sudo set_antenna ufl
echo "Done!"
sed -i -e '$i \set_antenna ufl\n' /etc/rc.local
echo "Done!"

#Updates operating system
echo "Updating OS..."
sudo apt-get update
sudo apt-get upgrade
echo "Done!"

#Installs Python
echo "Installing Python..."
sudo apt-get install python
echo "Done!"

#Installs the unnoficial CHIP_IO v5.5 package
echo "Installing CHIP_IO..."
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
curl -o homebot.py https://raw.githubusercontent.com/Jalonzpa/homebot_code/master/homebot.py
chmod +x homebot.py
echo "Installed!"
echo "Booting HomeBot..."
python homebot.py
