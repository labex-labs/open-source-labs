#!/bin/zsh
# Running our program shows that the goroutine-based
# state management example completes about 80,000
# total operations.
cd /home/labex/project
/usr/local/go/bin/go run stateful-goroutines.go | grep "readOps: 71708"