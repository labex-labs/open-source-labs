#!/bin/bash
grep -q "mysyms" ~/.python_history && grep -q "symlist" ~/.python_history && grep -q "append" ~/.python_history && echo "True"
