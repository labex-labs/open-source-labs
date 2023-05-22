#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git init") && [ -d /home/labex/project/my_project/.git ] && echo "True"
  
