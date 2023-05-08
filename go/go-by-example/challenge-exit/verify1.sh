#!/bin/zsh
#  If you run `exit.go` using `/usr/local/go/bin/go run`, the exit
# will be picked up by `go` and printed.
cd /home/labex/project
/usr/local/go/bin/go run exit.go | grep "exit status 3"
