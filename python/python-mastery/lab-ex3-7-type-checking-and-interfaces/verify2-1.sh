#!/bin/bash

if grep -q "from abc import ABC, abstractmethod" /home/labex/project/tableformat.py; then
  if grep -q "class TableFormatter(ABC)" /home/labex/project/tableformat.py; then
    if grep -q "@abstractmethod" /home/labex/project/tableformat.py; then
      echo "Success! TableFormatter is now a proper abstract base class."
      exit 0
    else
      echo "The @abstractmethod decorator is missing."
      exit 1
    fi
  else
    echo "TableFormatter is not inheriting from ABC."
    exit 1
  fi
else
  echo "Missing import from the abc module."
  exit 1
fi
