#!/bin/bash
grep -q "__slots__" ~/.python_history && echo "True"
