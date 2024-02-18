#!/bin/zsh

wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh

# Initialize .zsh_history
touch /home/labex/.zsh_history
