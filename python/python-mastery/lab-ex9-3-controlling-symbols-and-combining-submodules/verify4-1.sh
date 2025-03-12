#!/bin/bash
if [ -d "/home/labex/project/structly/tableformat" ] \
  && [ -d "/home/labex/project/structly/tableformat/formats" ] \
  && [ -f "/home/labex/project/structly/tableformat/formatter.py" ] \
  && [ -f "/home/labex/project/structly/tableformat/formats/text.py" ] \
  && [ -f "/home/labex/project/structly/tableformat/formats/csv.py" ] \
  && [ -f "/home/labex/project/structly/tableformat/formats/html.py" ] \
  && [ -f "/home/labex/project/structly/tableformat/__init__.py" ] \
  && [ -f "/home/labex/project/structly/tableformat/formats/__init__.py" ]; then
  exit 0
else
  exit 1
fi
