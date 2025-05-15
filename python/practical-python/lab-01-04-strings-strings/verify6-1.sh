#!/bin/bash
(grep -q "replace" ~/.python_history && grep -q "strip" ~/.python_history && grep -q "lower" ~/.python_history && grep -q "upper" ~/.python_history) && echo "True"
