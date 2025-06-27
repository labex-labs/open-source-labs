#!/bin/bash

cd /home/labex/project

if grep -q "from .validate import validate_type" "structly/structure.py"; then
  echo "Import statement in structure.py has been updated correctly."
  exit 0
else
  echo "Import statement in structure.py has not been updated correctly. It should be: from .validate import validate_type"
  exit 1
fi
