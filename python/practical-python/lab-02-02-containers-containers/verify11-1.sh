#!/bin/bash
(python3 ~/project/report.py > debug2 && grep "106.28" debug2) && echo "True"
