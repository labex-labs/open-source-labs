#!/bin/zsh
cd /home/labex/project
/usr/local/go/bin/go run generics.go | grep "keys: [4 1 2]"
