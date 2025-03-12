#!/bin/bash
# Check if portfolio.csv has been accessed
grep -q "portfolio.csv" ~/.python_history \
  && grep -q "csv.reader" ~/.python_history \
  && grep -q "pprint" ~/.python_history \
  && grep -q "for " ~/.python_history \
  && grep -q "defaultdict" ~/.python_history && echo "Success" || echo "Failure: Make sure you've executed all the commands in Step 1"
