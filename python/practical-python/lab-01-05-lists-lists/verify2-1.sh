#!/bin/bash
grep -q "insert" ~/.python_history && grep -q "append" ~/.python_history && echo "True"
