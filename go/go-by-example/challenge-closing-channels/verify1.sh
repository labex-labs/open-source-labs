#!/bin/zsh
cd /home/labex/project
/usr/local/go/bin/go run closing-channels.go | grep "sent job 1"