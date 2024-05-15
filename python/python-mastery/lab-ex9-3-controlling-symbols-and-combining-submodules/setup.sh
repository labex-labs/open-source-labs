#!/bin/zsh

wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
cd ~/project && mkdir structly && unzip structly.zip -d ./structly && rm structly.zip
