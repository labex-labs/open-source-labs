#!/bin/bash
grep -q "import" ~/.python_history && grep -q "is" ~/.python_history && grep -q "deepcopy" ~/.python_history && echo "True"
