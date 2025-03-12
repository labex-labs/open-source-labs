#!/bin/bash

if [ ! -f "/home/labex/project/validate.py" ]; then
  echo "validate.py file not found."
  exit 1
fi

if grep -q "class Typed" "/home/labex/project/validate.py" \
  && grep -q "expected_type = object" "/home/labex/project/validate.py" \
  && grep -q "_typed_classes" "/home/labex/project/validate.py" \
  && grep -q "globals().update" "/home/labex/project/validate.py"; then
  exit 0
else
  echo "Could not verify Typed class implementation and dynamic class generation."
  exit 1
fi
