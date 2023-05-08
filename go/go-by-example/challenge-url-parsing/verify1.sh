#!/bin/zsh
# Running our URL parsing program shows all the different
# pieces that we extracted.
cd /home/labex/project
go run url-parsing.go | grep "postgres"