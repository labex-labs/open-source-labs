#!/bin/zsh
# Our running program shows the 5 jobs being executed by
# various workers. The program only takes about 2 seconds
# despite doing about 5 seconds of total work because
# there are 3 workers operating concurrently.
cd /home/labex/project
time /usr/local/go/bin/go run worker-pools.go | grep "worker 1 started  job 1"
