#!/bin/zsh
(cat /home/labex/project/stock.py | grep -q "from typedproperty import typedproperty") && (cat /home/labex/project/typedproperty.py | grep -q "typedproperty") && echo "true"