#!/bin/bash
# To experiment with command-line arguments it's best to
# build a binary with `go build` first.
cd /home/labex/project
/usr/local/go/bin/go build command-line-arguments.go | grep "cd /home/labex/project"
