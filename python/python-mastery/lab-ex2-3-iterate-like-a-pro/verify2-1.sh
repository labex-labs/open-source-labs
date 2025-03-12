#!/bin/bash
grep -q "enumerate" ~/.python_history \
  && grep -q "zip" ~/.python_history \
  && grep -q "dict(zip" ~/.python_history && echo "Success" || echo "Failure: Make sure you've executed the commands with enumerate() and zip() functions in Step 2"
