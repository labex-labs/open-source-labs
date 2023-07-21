#!/bin/zsh
 (cd home/labex/project/git-playground && git config core.eol | grep "lf") && echo "True"
