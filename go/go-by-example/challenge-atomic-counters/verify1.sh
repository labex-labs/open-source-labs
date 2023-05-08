#!/bin/zsh
# We expect to get exactly 50,000 operations. Had we
# used the non-atomic `ops++` to increment the counter,
# we'd likely get a different number, changing between
# runs, because the goroutines would interfere with
# each other. Moreover, we'd get data race failures
# when running with the `-race` flag.
cd /home/labex/project
/usr/local/go/bin/go run atomic-counters.go | grep "ops: 50000"