#!/bin/bash
if [[ -f file_readable.sh ]] && [[ -r test_file.txt ]]; then
  exit 0
else
  exit 1
fi
