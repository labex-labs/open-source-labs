#!/bin/bash
(cd /home/labex/project/git-playground && git log origin/master | grep "new feature") && echo "True"
