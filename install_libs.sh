#! /bin/bash
sudo apt-get install python-pip
sudo pip install virtualenv
virtualenv --distribute venv
source venv/bin/activate
pip install twilio
pip install cssselect
deactivate
cd src
ln -i -s ../venv/lib/python2.7/site-packages/twilio .
ln -i -s ../venv/lib/python2.7/site-packages/httplib2 .
ln -i -s ../venv/lib/python2.7/site-packages/six.py .
ln -i -s ../venv/lib/python2.7/site-packages/cssselect .
