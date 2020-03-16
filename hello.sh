#! /bin/bash

sudo apt-get -y update
mkdir py
cd py
sudo apt-get -y install python3-pip
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install flask 
sudo apt-get -y install gcc python3-dev
pip install psutil 
git clone https://github.com/yonasjonas/flaskapp.git
