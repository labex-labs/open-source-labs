#!/bin/bash

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash

# Create backup directory if it doesn't exist
mkdir -p /home/labex/project/backup
