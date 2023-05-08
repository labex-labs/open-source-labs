#!/bin/zsh
cd /home/labex/project
/usr/local/go/bin/go run channel-directions.go | grep "passed message"