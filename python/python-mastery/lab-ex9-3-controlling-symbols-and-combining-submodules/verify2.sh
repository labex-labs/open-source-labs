#!/bin/zsh

cat /home/labex/project/structly/__init__.py | grep -E "from.*import"
cat /home/labex/project/structly/__init__.py | grep -E "__all__.*="
cat /home/labex/project/stock.py | grep -E "from[^.].*import"
cat /home/labex/project/structly/structure.py | grep -E "__all__.*="
cat /home/labex/project/structly/reader.py | grep -E "__all__.*="
cat /home/labex/project/structly/tableformat.py | grep -E "__all__.*="
