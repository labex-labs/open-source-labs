#!/bin/zsh

cat /home/labex/project/server.py | grep "types"
cat /home/labex/project/server.py | grep -E "@.*coroutine"
cat /home/labex/project/server.py | grep "async"
cat /home/labex/project/server.py | grep "await"
