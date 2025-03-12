#!/bin/bash
grep -q "import simplemod" ~/.python_history \
  && (grep -q "simplemod.foo" ~/.python_history || grep -q "foo\(\)" ~/.python_history) \
  && exit 0 || exit 1
