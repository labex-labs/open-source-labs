#!/bin/bash
grep -q "pass" ~/.python_history && grep -q "if" ~/.python_history && echo "True"
