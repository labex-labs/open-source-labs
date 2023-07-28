#!/bin/zsh

cat /home/labex/project/server.py | grep "class"
cat /home/labex/project/server.py | grep "__init__"
cat /home/labex/project/server.py | grep "__getattr__"
cat /home/labex/project/server.py | grep "recv"
cat /home/labex/project/server.py | grep "accept"
cat /home/labex/project/server.py | grep "send"
