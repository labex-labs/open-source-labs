#!/bin/zsh
cd /tmp
cp /home/labex/project/directory_exist.sh .
echo "testdir" | bash directory_exist.sh
ls | grep "testdir"