#!/bin/zsh
# Try running the file-writing code.
cd /home/labex/project
/usr/local/go/bin/go run writing-files.go | grep "wrote 5 bytes"