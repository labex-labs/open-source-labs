#!/bin/bash
grep -q "importlib.reload" ~/.python_history \
  && grep -q "isinstance" ~/.python_history \
  && exit 0 || exit 1
