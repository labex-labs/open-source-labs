#!/bin/bash
[ -f ~/project/reader.py ] \
  && grep -q "read_csv_as_dicts" ~/project/reader.py \
  && grep -q "import csv" ~/project/reader.py
