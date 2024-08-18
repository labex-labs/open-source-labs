#!/bin/bash
if [[ $(pwd) == "/home/labex/project" ]]; then
  exit 0
else
  exit 1
fi
