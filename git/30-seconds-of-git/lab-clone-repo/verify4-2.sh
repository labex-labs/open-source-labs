#!/bin/bash
cd /home/labex/project/shallow-repo
[[ $(git rev-list --count HEAD) -eq 1 ]]
