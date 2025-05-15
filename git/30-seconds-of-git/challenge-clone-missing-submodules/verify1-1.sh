#!/bin/bash
(cd /home/labex/project/git && git submodule status | grep "(") && (cd /home/labex/project/git && git submodule status | grep ")") && (cd /home/labex/project/git && git submodule foreach git status | grep "nothing to commit, working tree clean") && echo "True"
