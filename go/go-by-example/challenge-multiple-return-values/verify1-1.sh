#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run multiple-return-values.go | grep "3"
