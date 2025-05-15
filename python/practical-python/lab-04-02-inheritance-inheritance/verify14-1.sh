#!/bin/bash
(cat /home/labex/project/tableformat.py | grep -q "def create_formatter") && echo "True"
