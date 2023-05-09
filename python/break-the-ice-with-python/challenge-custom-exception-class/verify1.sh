#!/bin/zsh

cd /tmp && python3 custom_exception_class_test.py && echo 123
cat /home/labex/project/custom_exception_class.py | grep -E "try:"
cat /home/labex/project/custom_exception_class.py | grep -E "except:"
