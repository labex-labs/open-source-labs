#!/bin/bash
(python3 ~/project/report.py > debug1 && grep "30.34" debug1) && echo "True"
