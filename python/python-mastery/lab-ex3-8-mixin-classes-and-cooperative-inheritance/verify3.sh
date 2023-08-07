#!/bin/zsh


cat /home/labex/project/tableformat.py | grep -E 'class.*\(.*ColumnFormatMixin'
cat /home/labex/project/tableformat.py | grep -E 'class.*\(.*UpperHeadersMixin'
cat ~/.python_history | grep "create_formatter"
