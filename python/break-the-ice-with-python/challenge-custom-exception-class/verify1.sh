#!/bin/zsh

cd /tmp                                                                                                           
echo "123" | python3 custom_exception_class_test.py
cat /home/labex/project/custom_exception_class.py | grep -E "try:"
