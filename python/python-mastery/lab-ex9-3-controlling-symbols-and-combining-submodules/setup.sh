#!/bin/zsh

cd /tmp && wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
cd /home/labex/project && mkdir -p structly && wget -q https://labex-data.s3.amazonaws.com/structly.zip && unzip -q structly.zip -d ./structly && rm structly.zip
