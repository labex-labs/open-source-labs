#!/bin/zsh
# Running our program prints the sorted string and int
# slices and `true` as the result of our `AreSorted` test.
cd /home/labex/project
/usr/local/go/bin/go run sorting.go | grep "Strings: [a b c]"
