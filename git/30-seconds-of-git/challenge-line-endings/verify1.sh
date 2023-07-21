#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git config core.eol lf") && (cd /home/labex/project/git-playground && git config core.eol | grep "lf") && echo "True"
