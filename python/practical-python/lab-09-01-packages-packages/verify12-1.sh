#!/bin/bash
cd /home/labex/project/porty-app && python3 -m porty.report /home/labex/project/porty-app/portfolio.csv /home/labex/project/porty-app/prices.csv txt > debug1 && grep "MSFT" debug1
