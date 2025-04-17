#!/bin/bash

cd /home/labex/project
grep -q "@shares.setter" stock.py && grep -q "raise TypeError" stock.py && grep -q "raise ValueError" stock.py
