#!/bin/zsh
# Note that arrays appear in the form `[v1 v2 v3 ...]`
# when printed with `fmt.Println`.
cd /home/labex/project
go run arrays.go | grep "emp: [0 0 0 0 0]"