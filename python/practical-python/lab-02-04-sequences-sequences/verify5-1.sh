#!/bin/bash
(cat ~/.python_history | grep "for") && (cat ~/.python_history | grep "in") && (cat ~/.python_history | grep "print") && echo "True"
