#!/bin/bash
if grep -q "__all__" /home/labex/project/structly/__init__.py \
  && grep -q "Structure" /home/labex/project/structly/__init__.py \
  && grep -q "read_csv_as_instances" /home/labex/project/structly/__init__.py \
  && grep -q "create_formatter" /home/labex/project/structly/__init__.py \
  && grep -q "print_table" /home/labex/project/structly/__init__.py; then
  exit 0
else
  exit 1
fi
