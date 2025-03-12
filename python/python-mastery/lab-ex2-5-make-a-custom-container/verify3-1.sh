#!/bin/bash
grep -E "read_rides_as_columns|tracemalloc" ~/project/readrides.py && echo "Success!" || echo "Couldn't find the read_rides_as_columns function or tracemalloc in readrides.py."
