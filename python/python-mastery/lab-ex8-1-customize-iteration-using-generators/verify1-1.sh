#!/bin/bash
# Check if the Python history contains the frange function definition and usage
grep -q "def frange" ~/.python_history && echo "Success" || echo "Failure: Make sure you defined the frange generator function"
