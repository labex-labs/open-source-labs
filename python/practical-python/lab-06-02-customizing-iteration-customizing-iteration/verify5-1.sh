#!/bin/bash
(cat /home/labex/project/follow.py | grep -q "__main__") && echo "true"
