#!/bin/bash
(grep -q "len" ~/.python_history && grep -q "+" ~/.python_history && grep -q "in" ~/.python_history && grep -q "not in" ~/.python_history) && echo "True"
