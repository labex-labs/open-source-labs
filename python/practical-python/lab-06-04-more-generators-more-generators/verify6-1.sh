#!/bin/bash
(! cat /home/labex/project/ticker.py | grep -q "yield dict(zip(") && echo "true"
