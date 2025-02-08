#!/bin/zsh
cd /home/labex/project
/usr/local/go/bin/go run functions.go | grep "1+2 = 3"
