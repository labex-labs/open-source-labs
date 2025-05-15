#!/bin/bash
grep -q "int" ~/.python_history && grep -q "float" ~/.python_history && echo "True"
