#!/bin/bash
grep -q "__init__" /home/labex/project/structure.py \
  && grep -q "len" /home/labex/project/structure.py \
  && grep -q "TypeError" /home/labex/project/structure.py \
  && grep -q "setattr" /home/labex/project/structure.py
