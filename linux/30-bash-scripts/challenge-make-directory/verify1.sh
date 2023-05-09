#!/bin/zsh
cd /tmp
cp /home/labex/project/make_directory.sh .
echo "testdir" | bash make_directory.sh
ls | grep "testdir"
