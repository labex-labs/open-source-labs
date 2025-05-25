#!/bin/bash
(cd /home/labex/project/git-playground && git config --list | grep "name") && echo "True"
