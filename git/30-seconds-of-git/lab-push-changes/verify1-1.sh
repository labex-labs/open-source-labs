#!/bin/bash
(cd /home/labex/project/git-playground && git log origin/master | grep "Added new feature") && echo "True"
