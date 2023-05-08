#!/bin/zsh
# When we run our program it is replaced by `ls`.
cd /home/labex/project
go run execing-processes.go | grep "total 16"