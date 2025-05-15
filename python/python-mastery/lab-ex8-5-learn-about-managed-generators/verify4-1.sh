#!/bin/bash

ls -la /home/labex/project/server.py
cat /home/labex/project/server.py | grep "from socket import"
cat /home/labex/project/server.py | grep "from select import select"
cat /home/labex/project/server.py | grep "from collections import deque"
cat /home/labex/project/server.py | grep "recv_wait"
cat /home/labex/project/server.py | grep "send_wait"
