#!/bin/bash

cat /home/labex/project/server.py | grep "def tcp_server"
cat /home/labex/project/server.py | grep "def echo_handler"
cat /home/labex/project/server.py | grep "sock.listen"
cat /home/labex/project/server.py | grep "client.send"
cat /home/labex/project/server.py | grep "__main__"
