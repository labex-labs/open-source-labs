#!/bin/zsh
cd /home/labex/project
go run non-blocking-channel-operations.go | grep "no message received"