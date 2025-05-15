#!/bin/bash
(grep -q ">100" ~/.python_history || grep -q "> 100" ~/.python_history) && echo "True"
