#!/bin/zsh

(cat ~/.zsh_history | grep -v grep | grep -w "git commit") && (cat ~/.zsh_history | grep -v grep | grep 'git config --global core.editor "vim"') && (cd /home/labex/project/git-playground && cat hello.txt | grep "Hello, Git") && (cd /home/labex/project/git-playground && git log | grep "Update hello.txt") && echo "True"