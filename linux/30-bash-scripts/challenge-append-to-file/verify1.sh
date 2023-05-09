#!/bin/zsh
cd /tmp
cp /home/labex/project/append_file.sh .
bash append_file.sh
cat book.txt | grep "Laravel"
