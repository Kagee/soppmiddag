#! /bin/bash
sudo apt-get install python-pip
sudo pip install virtualenv
# Check if folder exsists, and act
# accordingly
if [ ! -d "venv" ]; then
    virtualenv --distribute venv
fi
source venv/bin/activate
pip install twilio
pip install cssselect
deactivate
cd src
ln -i -s ../venv/lib/python2.7/site-packages/twilio .
ln -i -s ../venv/lib/python2.7/site-packages/httplib2 .
ln -i -s ../venv/lib/python2.7/site-packages/six.py .
ln -i -s ../venv/lib/python2.7/site-packages/cssselect .
