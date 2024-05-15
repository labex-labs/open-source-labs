#!/bin/zsh
python3 /home/labex/project/mortgage.py > debug && cat /home/labex/project/mortgage.py | less -R | grep "f'" && echo "True"
