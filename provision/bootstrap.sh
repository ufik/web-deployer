#!/bin/bash

sudo su
apt-get install git tig -y

debconf-set-selections <<< 'mysql-server mysql-server/root_password password test'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password test'
apt-get -y install mysql-server

touch /etc/apt/sources.list.d/fkrull-daedsnakes-jessie.list

echo 'deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu trusty main' > /etc/apt/sources.list.d/fkrull-daedsnakes-jessie.list
echo 'deb-src http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu trusty main' >> /etc/apt/sources.list.d/fkrull-daedsnakes-jessie.list

gpg --keyserver keyserver.ubuntu.com --recv-keys DB82666C
gpg --export DB82666C | apt-key add -

apt-get update
apt-get install python3.5 -y

rm /usr/bin/python
ln -s /usr/bin/python3.5 /usr/bin/python

# install pip
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

rm get-pip.py

# install django
pip install Django
pip install djangorestframework
pip install py-moneyed django-money
pip install websockets
pip install -U python-digitalocean
pip install PyMySQL

export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/

mysqladmin -u root -ptest create deployer