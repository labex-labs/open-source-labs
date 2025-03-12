#!/bin/bash
if grep -q "from collections import Counter" ~/.python_history && grep -q "from collections import defaultdict" ~/.python_history && grep -q "byname.*defaultdict" ~/.python_history; then
  exit 0
else
  exit 1
fi
