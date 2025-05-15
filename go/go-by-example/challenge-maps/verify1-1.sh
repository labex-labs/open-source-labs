#!/bin/bash
# Note that maps appear in the form `map[k:v k:v]` when
# printed with `fmt.Println`.
cd /home/labex/project
/usr/local/go/bin/go run maps.go | grep "map: map[k1:7 k2:13]"
