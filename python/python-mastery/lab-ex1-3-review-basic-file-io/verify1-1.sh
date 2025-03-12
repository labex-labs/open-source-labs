#!/bin/zsh

if [ -f ~/project/portfolio.dat ]; then
  echo "portfolio.dat exists"
else
  exit 1
fi
