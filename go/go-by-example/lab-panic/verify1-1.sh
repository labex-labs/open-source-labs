#!/bin/bash
# Running this program will cause it to panic, print
# an error message and goroutine traces, and exit with
# a non-zero status.

# When first panic in `main` fires, the program exits
# without reaching the rest of the code. If you'd like
# to see the program try to create a temp file, comment
# the first panic out.
cd /home/labex/project
/usr/local/go/bin/go run panic.go | grep "panic: a problem"
