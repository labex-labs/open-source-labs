#!/bin/bash
grep -q "symlist.index" ~/.python_history && grep -q "symlist.append" ~/.python_history && grep -q "symlist.insert" ~/.python_history && echo "True"
