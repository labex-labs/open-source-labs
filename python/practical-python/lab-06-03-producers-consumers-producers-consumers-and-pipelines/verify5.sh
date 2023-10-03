#!/bin/zsh
python3 /home/labex/project/ticket.py > debug && grep -q "change" && echo "true"
