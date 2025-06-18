#!/bin/bash
# Running our program we see the first batch of requests
# handled once every ~200 milliseconds as desired.
cd /home/labex/project
/usr/local/go/bin/go run rate-limiting.go
