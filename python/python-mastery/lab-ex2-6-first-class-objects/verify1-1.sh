#!/bin/bash
grep -q "coltypes" ~/.python_history \
  && grep -q "zip" ~/.python_history \
  && grep -q "func" ~/.python_history
