#!/bin/bash
if grep -q "__all__" /home/labex/project/structly/structure.py \
  && grep -q "__all__" /home/labex/project/structly/reader.py \
  && grep -q "__all__" /home/labex/project/structly/tableformat.py \
  && grep -q "from .structure import \*" /home/labex/project/structly/__init__.py \
  && grep -q "from .reader import \*" /home/labex/project/structly/__init__.py \
  && grep -q "from .tableformat import \*" /home/labex/project/structly/__init__.py; then
  exit 0
else
  exit 1
fi
