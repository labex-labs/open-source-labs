#!/bin/bash
if [ -f /home/labex/project/teststock.py ]; then
  grep -q "assertRaises" /home/labex/project/teststock.py \
    && grep -q "assertEqual" /home/labex/project/teststock.py \
    && grep -q "test_create" /home/labex/project/teststock.py \
    && grep -q "test_eq" /home/labex/project/teststock.py \
    && echo "Success" || echo "Failed: teststock.py is missing some test methods"
else
  echo "Failed: teststock.py file not found. Make sure you renamed test_stock.py back to teststock.py."
fi
