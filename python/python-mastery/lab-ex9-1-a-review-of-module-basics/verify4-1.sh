#!/bin/bash
grep -q "from simplemod import" ~/.python_history \
  && exit 0 || exit 1
