#!/bin/bash
(python3 /home/labex/project/portfolio.py) && (cat /home/labex/project/portfolio.py | grep -q "from_csv") && (cat /home/labex/project/report.py | grep -q "Portfolio\.from_csv") && echo "true"
