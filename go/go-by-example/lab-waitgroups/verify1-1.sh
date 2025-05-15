#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run waitgroups.go | grep "Worker 5 starting"
