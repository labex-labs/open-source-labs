#!/bin/bash
(cd /home/labex/project/git-playground && git checkout one-branch && git log | grep "Added some changes to README.md") && (cd /home/labex/project/git-playground && git checkout master && git log | grep "Added some changes to README.md") && (cd /home/labex/project/git-playground && git checkout master && ! git log | grep "merge") && echo "True"
