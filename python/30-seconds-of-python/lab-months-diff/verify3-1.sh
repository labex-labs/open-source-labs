#!/bin/zsh
cd ~/project && [ -f month_diff_test.py ] && grep -q 'from month_difference import months_diff' month_diff_test.py
