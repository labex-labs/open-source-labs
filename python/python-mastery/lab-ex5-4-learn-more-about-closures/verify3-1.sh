#!/bin/bash
if [ ! -f /home/labex/project/improved_typedproperty.py ]; then
  echo "improved_typedproperty.py file not found"
  exit 1
fi

if ! grep -q "class TypedProperty" /home/labex/project/improved_typedproperty.py; then
  echo "TypedProperty class not found in improved_typedproperty.py"
  exit 1
fi

if ! grep -q "__set_name__" /home/labex/project/improved_typedproperty.py; then
  echo "__set_name__ method not found in improved_typedproperty.py"
  exit 1
fi

if ! grep -q "def String" /home/labex/project/improved_typedproperty.py; then
  echo "String function not found in improved_typedproperty.py"
  exit 1
fi

exit 0
