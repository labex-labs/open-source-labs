#!/bin/bash
grep -q "print" ~/.python_history && grep -q "]" ~/.python_history && echo "True"
