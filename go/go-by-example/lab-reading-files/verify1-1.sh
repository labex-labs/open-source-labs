#!/bin/bash
cd /home/labex/project
echo "hello" > /tmp/dat
cd /home/labex/project
echo "go" >> /tmp/dat
cd /home/labex/project
/usr/local/go/bin/go run reading-files.go | grep "hello"
