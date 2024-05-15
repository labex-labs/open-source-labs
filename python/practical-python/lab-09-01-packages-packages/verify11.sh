#!/bin/zsh
cat /home/labex/project/porty/report.py | grep "from \." || cat /home/labex/project/porty-app/porty/report.py | grep "from \."
