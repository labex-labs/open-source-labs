#!/bin/zsh
cd /home/labex/project
/usr/local/go/bin/go build command-line-subcommands.go | grep ""
