#!/bin/bash
grep -q "print" ~/.python_history && grep -q "as" ~/.python_history && grep -q "open" ~/.python_history && grep -q "import gzip" ~/.python_history && grep -q "with" ~/.python_history && echo "True"
