#!/bin/bash
grep -q "validators = {}" /home/labex/project/validate.py && grep -q "__init_subclass__" /home/labex/project/validate.py
exit $?
