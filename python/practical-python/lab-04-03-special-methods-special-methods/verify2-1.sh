#!/bin/bash
grep -q "from" ~/.python_history && grep -q "str" ~/.python_history && grep -q "repr" ~/.python_history && echo "True"
