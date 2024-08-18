#!/bin/zsh
if grep -q "#!/bin/bash" ~/project/array-comparison.sh; then
  exit 0
else
  exit 1
fi
