#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run number-parsing.go | grep "1.234"
