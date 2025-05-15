#!/bin/bash
(cat /home/labex/project/follow.py | grep -q "import report") && echo "true"
