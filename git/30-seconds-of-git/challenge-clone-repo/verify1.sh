#!/bin/zsh
(cd /home/labex/project/my-project && cat ~/.zsh_history | grep -v grep | grep "git clone") && (cd /home/labex/project/my-project && git status | grep "On branch master" >/dev/null) && echo "True"


