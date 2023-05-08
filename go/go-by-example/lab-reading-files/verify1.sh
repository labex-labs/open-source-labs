#!/bin/zsh
cd /home/labex/project
echo "hello" > /tmp/dat
cd /home/labex/project
echo "go" >>   /tmp/dat
cd /home/labex/project
go run reading-files.go | grep "hello"