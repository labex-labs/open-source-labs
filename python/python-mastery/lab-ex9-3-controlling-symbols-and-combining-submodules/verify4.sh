#!/bin/zsh

ls /home/labex/project/structly/tableformat
ls /home/labex/project/structly/tableformat/__init__.py
ls /home/labex/project/structly/tableformat/*/__init__.py
cat /home/labex/project/structly/tableformat/*/*/*.py | grep -E "from.*\.\..*import"
