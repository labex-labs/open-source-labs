#!/bin/bash
grep -q "prices = {" ~/.python_history || grep -q "prices={" ~/.python_history && echo "True"
