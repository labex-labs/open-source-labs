#!/bin/bash
python3 /tmp/test7.py && grep -q "for" ~/.python_history && echo "True"
