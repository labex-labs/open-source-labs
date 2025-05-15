#!/bin/bash
grep -q "def" ~/.python_history && grep -q "for" ~/.python_history && echo "True"
