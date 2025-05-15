#!/bin/bash
(cat /home/labex/project/fileparse.py | grep -q "import logging") || (grep -q "import logging" ~/.python_history)
