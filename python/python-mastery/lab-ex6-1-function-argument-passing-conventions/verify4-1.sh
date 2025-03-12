#!/bin/bash
grep -q "__setattr__" /home/labex/project/structure.py \
  && grep -q "startswith" /home/labex/project/structure.py \
  && grep -q "super()" /home/labex/project/structure.py \
  && grep -q "AttributeError" /home/labex/project/structure.py
