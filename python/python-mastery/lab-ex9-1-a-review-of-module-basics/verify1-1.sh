#!/bin/bash
if [ -f /home/labex/project/simplemod.py ]; then
  grep -q "x = 42" /home/labex/project/simplemod.py \
    && grep -q "def foo" /home/labex/project/simplemod.py \
    && grep -q "class Spam" /home/labex/project/simplemod.py \
    && grep -q "print" /home/labex/project/simplemod.py \
    && exit 0 || exit 1
else
  exit 1
fi
