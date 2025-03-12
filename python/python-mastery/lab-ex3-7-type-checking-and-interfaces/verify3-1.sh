#!/bin/bash

if grep -q "class CSVParser(ABC)" /home/labex/project/reader.py; then
  if grep -q "class DictCSVParser(CSVParser)" /home/labex/project/reader.py; then
    if grep -q "class InstanceCSVParser(CSVParser)" /home/labex/project/reader.py; then
      if grep -q "parser = DictCSVParser" /home/labex/project/reader.py && grep -q "parser = InstanceCSVParser" /home/labex/project/reader.py; then
        echo "Success! The CSVParser classes have been implemented and the read functions have been refactored."
        exit 0
      else
        echo "The read functions have not been refactored to use the parser classes."
        exit 1
      fi
    else
      echo "The InstanceCSVParser class is missing."
      exit 1
    fi
  else
    echo "The DictCSVParser class is missing."
    exit 1
  fi
else
  echo "The CSVParser abstract base class is missing."
  exit 1
fi
