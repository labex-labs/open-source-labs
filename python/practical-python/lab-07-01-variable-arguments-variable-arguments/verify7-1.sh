#!/bin/bash
(cat /home/labex/project/report.py | grep -q "Stock(\*\*d)") && echo "true"
