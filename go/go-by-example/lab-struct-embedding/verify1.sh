#!/bin/zsh
cd /home/labex/project
/usr/local/go/bin/go run struct-embedding.go | grep "co={num: 1, str: some name}"
