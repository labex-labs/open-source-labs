#!/bin/zsh

cd /tmp && wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
cd ~/project && unzip ctabus.csv.zip && rm ctabus.csv.zip
