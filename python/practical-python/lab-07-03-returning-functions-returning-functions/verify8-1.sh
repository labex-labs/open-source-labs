#!/bin/bash
(cat /home/labex/project/typedproperty.py | grep -q "lambda") && echo "true"
