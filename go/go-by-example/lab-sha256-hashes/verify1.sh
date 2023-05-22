#!/bin/zsh
# Running the program computes the hash and prints it in
# a human-readable hex format.
cd /home/labex/project
/usr/local/go/bin/go run sha256-hashes.go | grep "sha256 this string"
