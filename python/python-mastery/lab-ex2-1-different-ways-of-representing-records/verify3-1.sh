#!/bin/bash
ls /home/labex/project/readrides.py > /dev/null 2>&1 && grep -q "read_rides_as_tuples" /home/labex/project/readrides.py && echo "Success"
