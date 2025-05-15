#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run range-over-channels.go | grep "one"
