#!/bin/bash
(python3 ~/project/pcost.py > debug1 && cat ~/project/pcost.py | grep "report.read_portfolio") && echo "True"
