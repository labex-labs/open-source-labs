#!/bin/bash
# We receive the values `"one"` and then `"two"` as
# expected.
cd /home/labex/project
time /usr/local/go/bin/go run select.go | grep "received one"
