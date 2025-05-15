#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run directories.go | grep "Listing subdir/parent"
