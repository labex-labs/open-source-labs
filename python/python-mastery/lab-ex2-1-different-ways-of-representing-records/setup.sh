#!/bin/zsh

wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
cd /home/labex/project && wget https://raw.githubusercontent.com/labex-labs/file-downloader/master/ctabus.csv.zip && unzip ctabus.csv.zip && rm ctabus.csv.zip
