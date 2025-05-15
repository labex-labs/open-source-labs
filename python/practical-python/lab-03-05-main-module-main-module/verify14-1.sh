#!/bin/bash
(cat ~/project/report.py | grep -q "#\!") && (cat ~/project/pcost.py | grep -q "#\!") && (cat ~/.zsh_history | grep -v grep | grep "./pcost.py") && (cat ~/.zsh_history | grep -v grep | grep "./report.py") && echo "true"
