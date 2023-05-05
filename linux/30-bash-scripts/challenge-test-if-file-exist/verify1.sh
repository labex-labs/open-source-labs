#!/bin/zsh
cd /home/labex/project
bash file_exist.sh "151515"| grep "not"
bash file_exist.sh "file_exist"| grep "exists"
