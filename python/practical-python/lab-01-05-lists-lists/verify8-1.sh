#!/bin/bash
grep -q "in symlist" ~/.python_history && grep -q "for" ~/.python_history && echo "True"
