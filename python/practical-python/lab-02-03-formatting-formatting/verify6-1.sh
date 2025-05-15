#!/bin/bash
grep -q "value" ~/.python_history && grep -q ":*>" ~/.python_history && echo "True"
