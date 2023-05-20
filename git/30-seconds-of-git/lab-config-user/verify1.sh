#!/bin/zsh
(cd /home/labex/project/git-playground && git config --list | grep " grep -q "user.email=jane.doe@example.com" >/dev/null) && (cd /home/labex/project/git-playground && git config --list | grep -q "user.name=Jane Doe" >/dev/null) && echo "True"
