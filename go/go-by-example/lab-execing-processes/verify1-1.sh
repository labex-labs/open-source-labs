#!/bin/bash
# When we run our program it is replaced by `ls`.
cd /home/labex/project
/usr/local/go/bin/go run execing-processes.go | grep "total 16"
