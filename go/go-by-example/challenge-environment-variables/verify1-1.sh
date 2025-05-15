#!/bin/bash
# Running the program shows that we pick up the value
# for `FOO` that we set in the program, but that
# `BAR` is empty.
cd /home/labex/project
/usr/local/go/bin/go run environment-variables.go | grep "FOO: 1"
