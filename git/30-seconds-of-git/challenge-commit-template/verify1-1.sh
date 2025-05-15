#!/bin/bash
(cd /home/labex/project/git-playground && git config commit.template | grep "commit-template") && (cd /home/labex/project/git-playground && cat /home/labex/project/git-playground/commit-template | grep "This creates a template with three sections") && echo "True"
