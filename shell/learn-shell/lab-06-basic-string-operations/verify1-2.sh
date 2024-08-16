#!/bin/bash
if grep -q "#!/bin/bash" ~/project/string_operations.sh; then
  exit 0
else
  exit 1
fi
