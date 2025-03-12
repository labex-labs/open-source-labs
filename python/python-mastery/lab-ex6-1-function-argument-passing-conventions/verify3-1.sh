#!/bin/bash
grep -q "__repr__" /home/labex/project/structure.py \
  && grep -q "type" /home/labex/project/structure.py \
  && grep -q "getattr" /home/labex/project/structure.py \
  && grep -q "join" /home/labex/project/structure.py
