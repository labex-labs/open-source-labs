#!/bin/bash
cd /home/labex/project && python3 test_key_of_max.py 2>&1 | grep -q OK
