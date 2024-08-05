#!/bin/bash
cd /home/labex/project/branch-repo
[[ $(git branch | wc -l) -eq 1 && $(git branch | grep -c "main") -eq 1 ]]
