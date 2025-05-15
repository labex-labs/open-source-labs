#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run recover.go | grep "Recovered. Error:"
