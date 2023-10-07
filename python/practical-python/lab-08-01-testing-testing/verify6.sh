#!/bin/zsh
(cat /home/labex/project/test_simple.py | grep "unittest\.main") && (cat ~/.zsh_history | grep -v grep | grep "test_simple\.py") && echo "true"


