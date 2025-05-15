#!/bin/bash
(cat /home/labex/project/stocklog.csv | grep -q "AAPL") && echo "true"
