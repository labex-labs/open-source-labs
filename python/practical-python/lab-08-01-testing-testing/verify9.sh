#!/bin/zsh
python3 /home/labex/project/test_stock.py && (cat /home/labex/project/test_stock.py | grep -q "stock.Stock") && echo "true"
