#!/bin/bash
grep -q "and" ~/.python_history && grep -q ">" ~/.python_history && echo "True"
