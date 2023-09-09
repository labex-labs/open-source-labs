#!/bin/zsh
(grep -q "num_bills * bill_thickness" ~/.python_history || grep -q "num_bills*bill_thickness" ~/.python_history) && grep -q "print" ~/.python_history && echo "True"
