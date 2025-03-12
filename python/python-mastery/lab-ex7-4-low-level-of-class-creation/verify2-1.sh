#!/bin/bash

if [ ! -f "/home/labex/project/structure.py" ]; then
  echo "structure.py file not found."
  exit 1
fi

if grep -q "def typed_structure" "/home/labex/project/structure.py" \
  && grep -q "cls = type(clsname" "/home/labex/project/structure.py" \
  && grep -q "return cls" "/home/labex/project/structure.py"; then
  exit 0
else
  echo "Could not verify typed_structure function implementation."
  exit 1
fi
