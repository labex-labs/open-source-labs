#!/bin/bash
grep -q "f'" ~/.python_history && grep -q "print" ~/.python_history && echo "True"
