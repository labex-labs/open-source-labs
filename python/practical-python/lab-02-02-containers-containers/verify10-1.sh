#!/bin/bash
(python3 ~/project/report.py > debug1 && grep "91.1}" debug1) && echo "True"
