#!/bin/bash
grep -q "intern" ~/.python_history \
  && grep -q "tracemalloc" ~/.python_history \
  && grep -q "routeids" ~/.python_history
