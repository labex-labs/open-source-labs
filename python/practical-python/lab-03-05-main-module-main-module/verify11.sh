#!/bin/zsh
(cat ~/project/prog.py | grep -q "#\!") && echo "True" 
