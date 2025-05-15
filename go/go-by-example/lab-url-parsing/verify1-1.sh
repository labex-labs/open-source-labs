#!/bin/bash
# Running our URL parsing program shows all the different
# pieces that we extracted.
cd /home/labex/project
/usr/local/go/bin/go run url-parsing.go | grep "postgres"
