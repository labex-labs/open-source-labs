#!/bin/bash
(python3 ~/project/fileparse_3.3.py > debug && grep "51.23" debug) && echo "True"
