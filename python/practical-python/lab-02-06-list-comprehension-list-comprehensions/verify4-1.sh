#!/bin/bash
grep -q "append" ~/.python_history && grep -q "if" ~/.python_history && echo "True"
