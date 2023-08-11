#!/bin/zsh
cd /home/labex/project
cat file_exist.sh "151515" | grep "not"
bash file_exist.sh "file_exist" | grep "exists"
