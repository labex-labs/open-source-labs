#!/bin/zsh
cd /tmp
cp /home/labex/project/delete_file.sh .
touch hello.txt
echo "hello.txt\ny" | bash delete_file.sh
[ ! -f "hello.txt" ]