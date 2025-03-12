#!/bin/bash
if grep -q "def read_csv_as_instances" ~/project/reader.py && grep -q "records.append(cls.from_row(row))" ~/project/reader.py; then
  exit 0
else
  exit 1
fi
