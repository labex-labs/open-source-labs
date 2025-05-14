#!/bin/zsh

# Create necessary directories
mkdir -p /home/labex/project

# Make project directory the default working directory
cd /home/labex/project

# Setup Python shell history
cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
