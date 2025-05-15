#!/bin/bash
grep -q "prices" ~/.python_history && grep -q "\[" ~/.python_history && grep -q "{" ~/.python_history && echo "True"
