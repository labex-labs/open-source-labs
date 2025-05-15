#!/bin/bash
grep -q "foo" ~/.python_history && grep -q "def" ~/.python_history && echo "True"
