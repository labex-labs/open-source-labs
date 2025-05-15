#!/bin/bash
python3 ~/project/fileparse.py && (! cat ~/project/fileparse.py | grep -q "open") && echo "True"
