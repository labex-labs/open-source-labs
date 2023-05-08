#!/bin/zsh
# Note that while slices are different types than arrays,
# they are rendered similarly by `fmt.Println`.
cd /home/labex/project
/usr/local/go/bin/go run slices.go | grep "emp: [  ]"