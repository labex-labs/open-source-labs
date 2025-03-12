#!/bin/bash
[ -f ~/project/colreader.py ] \
  && grep -q "DataCollection" ~/project/colreader.py \
  && grep -q "read_csv_as_columns" ~/project/colreader.py
