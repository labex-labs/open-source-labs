#!/bin/zsh
grep -q ".__class__.__mro__" ~/.python_history && echo "True"
