#!/bin/bash
# Running the program shows that the counters
# updated as expected.
cd /home/labex/project
/usr/local/go/bin/go run mutexes.go | grep "map[a:20000 b:10000]"
