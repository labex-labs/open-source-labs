#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run channel-synchronization.go | grep "working...done                  "
