#!/bin/bash
(cd /home/labex/project/git-playground && git config --list | grep -q "user.email=" > /dev/null) && (cd /home/labex/project/git-playground && git config --list | grep -q "user.name=" > /dev/null) && echo "True"
