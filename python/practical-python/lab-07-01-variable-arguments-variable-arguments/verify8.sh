#!/bin/zsh
(cat /home/labex/project/report.py|grep -q "\*\*opts") && echo "true"
