#!/bin/bash
(python3 ~/project/mortgage.py > debug4 && grep "880074" debug4) && echo "True"
