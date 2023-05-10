#!/bin/zsh
# Depending on where you run this sample, some of the
# generated numbers may be different. Note that on
# the Go playground seeding with `time.Now()` still
# produces deterministic results due to the way the
# playground is implemented.
cd /home/labex/project
/usr/local/go/bin/go run random-numbers.go | grep "81,87"
