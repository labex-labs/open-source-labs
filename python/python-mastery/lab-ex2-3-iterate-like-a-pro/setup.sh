#!/bin/zsh

wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
mkdir -p ~/project
cd ~/project && wget https://raw.githubusercontent.com/dabeaz-course/practical-python/master/Data/portfolio.csv
cd ~/project && wget https://raw.githubusercontent.com/dabeaz-course/practical-python/master/Data/readport.py
cd ~/project && wget https://raw.githubusercontent.com/dabeaz-course/practical-python/master/Data/readrides.py
cd ~/project && wget https://raw.githubusercontent.com/dabeaz-course/practical-python/master/Data/ctabus.csv.zip && unzip ctabus.csv.zip && rm ctabus.csv.zip
