#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run string-functions.go | grep "Contains:   true"
