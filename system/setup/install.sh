set -x 
UBO_HOME=/home/pi/ubo-sdk
export PATH=$PATH:~/.local/bin

###### Install debian packages ######
sudo apt install -y python3-pyaudio portaudio19-dev python-all-dev libpcap-dev build-essential python3-alsaaudio python3-picamera2

######### Install python package ====
#change following line to include system packages
# --system-site-packages: Give the virtual environment 
# access to the system site-packages dir.
python3 -m venv --system-site-packages ~/ubo-venv
. /home/pi/ubo-venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install --upgrade pip
python3.9 -m pip install -r $UBO_HOME/system/setup/requirements.txt

#######################################
# Install SeeedStudio for speakers
######################################
sudo /bin/bash $UBO_HOME/system/setup/install_seeedstudio.sh

#######################################
# Install EEPROM tools
######################################
sudo /bin/bash $UBO_HOME/system/setup/install_eeprom.sh

#######################################
# Install Infra Red tools
######################################
sudo apt install ir-keytable 

#######################################
# Update config files
######################################
sudo cp $UBO_HOME/system/boot/config.txt /boot/config.txt
sudo cp $UBO_HOME/system/etc/modprobe.d/snd-blacklist.conf /etc/modprobe.d/snd-blacklist.conf
#######################################
# Add systemd services
######################################
sudo /bin/bash ./start_services.sh
