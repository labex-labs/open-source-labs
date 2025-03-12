if [ -f /home/labex/project/teststock.py ]; then
  grep -q "test_create_keyword_args" /home/labex/project/teststock.py \
    && grep -q "test_cost" /home/labex/project/teststock.py \
    && grep -q "test_sell" /home/labex/project/teststock.py \
    && grep -q "test_from_row" /home/labex/project/teststock.py \
    && grep -q "test_repr" /home/labex/project/teststock.py \
    && grep -q "test_eq" /home/labex/project/teststock.py \
    && echo "Success" || echo "Failed: teststock.py doesn't contain all the required test methods"
else
  echo "Failed: teststock.py file not found"
fi
