#!/bin/zsh
cd /home/labex/project
/usr/local/go/bin/go run templates.go | grep "Value: some text"