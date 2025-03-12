#!/bin/zsh

# Check if structure.py exists and contains the create_init method
if ! grep -q "create_init" /home/labex/project/structure.py; then
  echo "Please add the create_init method to the Structure class in structure.py."
  exit 1
fi

# Check if exec is used in the create_init method
if ! grep -q "exec" /home/labex/project/structure.py; then
  echo "Please use exec() in your create_init method."
  exit 1
fi

# Run the tests to ensure the Stock class works correctly
cd /home/labex/project
python3 -m unittest test_structure.py

exit $?
