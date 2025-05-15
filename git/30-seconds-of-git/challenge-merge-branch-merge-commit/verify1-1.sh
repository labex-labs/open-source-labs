#!/bin/bash
(cd /home/labex/project/git-playground && git checkout feature-branch && git log | grep "Add new line to README.md") && (cd /home/labex/project/git-playground && git checkout master && git log | grep "Add new line to README.md") && (cd /home/labex/project/git-playground && git checkout master && git log | grep "Merge feature-branch") && echo "True"
