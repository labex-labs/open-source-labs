#!/bin/zsh

cat ~/.python_history | grep -E "from.*import"
cat ~/.python_history | grep "__module__"
cat ~/.python_history | grep -E  "simplemod.*\..*\(.*\)"
cat /home/labex/project/structly/tableformat/formatter.py | grep -E "@.*classmethod"
cat /home/labex/project/structly/tableformat/formatter.py | grep "__init_subclass__"
cat ~/.python_history | grep "TableFormatter"
cat /home/labex/project/structly/tableformat/formatter.py | grep "get"
