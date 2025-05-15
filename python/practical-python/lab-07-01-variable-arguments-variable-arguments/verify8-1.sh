#!/bin/bash
(cat /home/labex/project/report.py | grep -q "\*\*opts") && echo "true"
