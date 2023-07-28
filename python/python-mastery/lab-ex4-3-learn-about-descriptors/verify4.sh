#!/bin/zsh

ls /home/labex/project/validate.py | grep "__set_name__"
ls /home/labex/project/stock.py | grep -E "String.*\(\s*"
ls /home/labex/project/stock.py | grep -E "PositiveInteger.*\(\s*"
ls /home/labex/project/stock.py | grep -E "PositiveFloat.*\(\s*"
