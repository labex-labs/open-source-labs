#!/bin/bash
grep -q "next" ~/.python_history \
  && grep -q "yield" ~/.python_history \
  && grep -q "tracemalloc" ~/.python_history \
  && grep -q "get_traced_memory" ~/.python_history && echo "Success" || echo "Failure: Make sure you've executed all the commands for generator expressions in Step 3"
