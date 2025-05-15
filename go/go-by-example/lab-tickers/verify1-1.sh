#!/bin/bash
# When we run this program the ticker should tick 3 times
# before we stop it.
cd /home/labex/project
/usr/local/go/bin/go run tickers.go | grep "Tick at 2012-09-23 11:29:56.487625 -0700 PDT"
