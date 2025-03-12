#!/bin/bash
if [ ! -f /home/labex/project/mymeta.py ]; then
  echo "File mymeta.py not found"
  exit 1
fi

if ! grep -q "class mytype(type)" /home/labex/project/mymeta.py; then
  echo "mytype class definition not found in mymeta.py"
  exit 1
fi

if ! grep -q "class myobject(metaclass=mytype)" /home/labex/project/mymeta.py; then
  echo "myobject class definition not found in mymeta.py"
  exit 1
fi

exit 0
