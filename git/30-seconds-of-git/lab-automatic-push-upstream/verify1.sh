#!/bin/zsh
(cd /home/labex/project/git-playground && git config --list | grep "push.default=current") && (cd /home/labex/project/git-playground && git branch -r | grep "new-feature") && echo "True"

 
