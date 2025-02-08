#!/bin/zsh

ls /home/labex/project/*/__init__.py
ls /home/labex/project/*/ | grep "structure.py"
ls /home/labex/project/*/ | grep "validate.py"
ls /home/labex/project/*/ | grep "reader.py"
ls /home/labex/project/*/ | grep "tableformat.py"
cat /home/labex/project/stock.py | grep -e "from.*\..*import"
cat /home/labex/project/stock.py | grep "__main__"
cat /home/labex/project/stock.py | grep "read_csv_as_instances"
cat /home/labex/project/stock.py | grep "print_table"
