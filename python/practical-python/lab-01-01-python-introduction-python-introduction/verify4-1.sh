#!/bin/bash
(cat ~/.python_history | grep "75") && (cat ~/.python_history | grep "_") && echo "True"
