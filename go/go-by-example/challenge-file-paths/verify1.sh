#!/bin/zsh
cd /home/labex/project
/usr/local/go/bin/go run file-paths.go | grep "p: dir1/dir2/filename"