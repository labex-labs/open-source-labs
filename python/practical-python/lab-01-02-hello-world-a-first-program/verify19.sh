#!/bin/zsh
((cat ~/project/sears.py | grep "day = days + 1") || (cat ~/project/sears.py | grep "day=days+1"))  && echo "True"
