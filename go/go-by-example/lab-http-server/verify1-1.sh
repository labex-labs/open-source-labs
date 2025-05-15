#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run http-clients.go | grep "Response status: 200 OK"
