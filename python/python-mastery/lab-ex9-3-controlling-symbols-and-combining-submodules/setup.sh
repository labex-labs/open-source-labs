#!/bin/zsh

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
cd /home/labex/project && mkdir -p structly && wget -q https://labex-data.s3.amazonaws.com/structly.zip && unzip -q structly.zip -d ./structly && rm structly.zip
