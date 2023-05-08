#!/bin/zsh
cd /home/labex/project
go run http-clients.go | grep "Response status: 200 OK"