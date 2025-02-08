#!/bin/zsh
(cd /home/labex/project/git && ! git submodule status | grep "sha1collisiondetection") && echo "True"
