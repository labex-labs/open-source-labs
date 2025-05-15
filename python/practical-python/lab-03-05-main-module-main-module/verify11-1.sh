#!/bin/bash
(cat ~/project/prog.py | grep -q "#\!") && echo "True"
