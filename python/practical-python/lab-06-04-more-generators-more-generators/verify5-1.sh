#!/bin/bash
(! cat /home/labex/project/portfolio.py | grep -q "(\[s\.shares") && echo "true"
