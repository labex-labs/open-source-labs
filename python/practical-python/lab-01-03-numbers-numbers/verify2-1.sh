#!/bin/bash
grep -q "True" ~/.python_history && grep -q "False" ~/.python_history && echo "True"
