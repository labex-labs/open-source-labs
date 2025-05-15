#!/bin/bash
(grep -q "print" ~/.python_history || (cat ~/project/foo.py | grep -q "print")) && echo "True"
