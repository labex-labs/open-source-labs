#!/bin/bash
(cd /home/labex/project/my-project && git submodule status | grep git-playground) && echo "True"
