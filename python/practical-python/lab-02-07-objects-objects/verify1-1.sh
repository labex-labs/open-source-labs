#!/bin/bash
grep -q "=" ~/.python_history && grep -q "append" ~/.python_history && echo "True"
