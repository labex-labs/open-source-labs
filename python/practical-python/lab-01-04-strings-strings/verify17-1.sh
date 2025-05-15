#!/bin/bash
grep -q "import" ~/.python_history && grep -q "re" ~/.python_history && echo "True"
