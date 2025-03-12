if [ -f /home/labex/project/teststock.py ]; then
  grep -q "assertRaises" /home/labex/project/teststock.py \
    && grep -q "test_shares_type" /home/labex/project/teststock.py \
    && grep -q "test_shares_value" /home/labex/project/teststock.py \
    && grep -q "test_price_type" /home/labex/project/teststock.py \
    && grep -q "test_price_value" /home/labex/project/teststock.py \
    && grep -q "test_attribute_error" /home/labex/project/teststock.py \
    && echo "Success" || echo "Failed: teststock.py doesn't contain all the required exception test methods"
else
  echo "Failed: teststock.py file not found"
fi
