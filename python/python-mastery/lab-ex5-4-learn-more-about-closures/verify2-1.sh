#!/bin/bash
if [ ! -f /home/labex/project/typedproperty.py ]; then
  echo "typedproperty.py file not found"
  exit 1
fi

if ! grep -q "def typedproperty" /home/labex/project/typedproperty.py; then
  echo "typedproperty function not found in typedproperty.py"
  exit 1
fi

if ! grep -q "def String" /home/labex/project/typedproperty.py; then
  echo "String function not found in typedproperty.py"
  exit 1
fi

if ! grep -q "def Integer" /home/labex/project/typedproperty.py; then
  echo "Integer function not found in typedproperty.py"
  exit 1
fi

if ! grep -q "def Float" /home/labex/project/typedproperty.py; then
  echo "Float function not found in typedproperty.py"
  exit 1
fi

exit 0
