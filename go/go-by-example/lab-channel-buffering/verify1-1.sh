#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run channel-buffering.go | grep "buffered"
