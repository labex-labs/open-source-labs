#!/bin/bash
(cat ~/project/fileparse_3.8.py | grep 'raise RuntimeError("select argument requires column headers")') && echo "True"
