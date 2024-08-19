#!/bin/bash
if [[ -f dir_exists.sh ]] && [[ -d test_directory ]]; then
  exit 0
else
  exit 1
fi
