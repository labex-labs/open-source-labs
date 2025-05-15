#!/bin/bash
grep -q "items" ~/.python_history && grep -q "list(zip" ~/.python_history && grep -q "sorted" ~/.python_history && echo "True"
