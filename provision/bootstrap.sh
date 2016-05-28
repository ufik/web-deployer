#!/bin/bash

sudo apt-get install git tig -y

# install pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

rm get-pip.py

# install django
sudo pip install Django
sudo pip install djangorestframework
sudo pip install py-moneyed django-money
