#!/bin/bash
cd /home/labex/project
/usr/local/go/bin/go run non-blocking-channel-operations.go | grep "no message received"
