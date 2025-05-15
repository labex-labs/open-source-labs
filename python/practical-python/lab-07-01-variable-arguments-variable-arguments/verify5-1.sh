#!/bin/bash
grep -q "return" ~/.python_history && grep -q "float" ~/.python_history && echo "True"
