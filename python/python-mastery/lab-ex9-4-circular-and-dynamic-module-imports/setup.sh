#!/bin/zsh

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
cd ~/project && mkdir structly && unzip structly.zip -d ./structly && rm structly.zip
