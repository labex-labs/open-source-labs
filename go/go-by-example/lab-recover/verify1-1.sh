#!/bin/zsh
cd /home/labex/project
/usr/local/go/bin/go run recover.go | grep "Recovered. Error:"
