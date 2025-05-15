#!/bin/bash
# The string encodes to slightly different values with the
# standard and URL base64 encoders (trailing `+` vs `-`)
# but they both decode to the original string as desired.
cd /home/labex/project
/usr/local/go/bin/go run base64-encoding.go | grep "YWJjMTIzIT8kKiYoKSctPUB+"
