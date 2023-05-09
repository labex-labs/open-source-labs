#!/bin/zsh

cd /tmp && python3 custom_exception_class_test.py
cat /home/labex/project/custom_exception_class.py | grep -E "try:"
cat /home/labex/project/custom_exception_class.py | grep -E "except:"
