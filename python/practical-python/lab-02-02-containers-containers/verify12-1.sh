#!/bin/bash
(python3 ~/project/report.py > debug3 && grep "Gain/Loss" debug3) && echo "True"
