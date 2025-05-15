#!/bin/bash
(cd /home/labex/project/git-playground && git log --name-status HEAD^..HEAD | grep "Empty commit") && echo "True"
