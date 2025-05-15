#!/bin/bash
if [ -f /home/labex/project/teststock.py ]; then
  grep -q "unittest" /home/labex/project/teststock.py && grep -q "TestStock" /home/labex/project/teststock.py && grep -q "test_create" /home/labex/project/teststock.py && grep -q "assertEqual" /home/labex/project/teststock.py && echo "Success" || echo "Failed: teststock.py doesn't contain the required test code"
else
  echo "Failed: teststock.py file not found"
fi
