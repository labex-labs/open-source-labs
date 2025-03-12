#!/bin/bash
grep -q "__getattr__" /home/labex/project/readonly_proxy.py && echo "Success" || echo "Fail: Cannot find __getattr__ method in readonly_proxy.py"
