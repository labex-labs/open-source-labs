#!/bin/bash
# Running our program shows a list sorted by string
# length, as desired.
cd /home/labex/project
/usr/local/go/bin/go run sorting-by-functions.go | grep "[kiwi peach banana]"
