#!/bin/bash
(cd /home/labex/project/git-playground && git branch -a | less -R | grep "remotes/origin/new-feature-1") && (cd /home/labex/project/git-playground && ! git branch -a | less -R | grep "remotes/origin/feature-branch") && echo "True"
