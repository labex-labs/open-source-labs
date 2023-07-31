#!/bin/zsh
(cd /home/labex/project/git-playground && git show HEAD~1 | less -R | grep "b/hello.txt") && (cd /home/labex/project/git-playground && git show HEAD~1 | less -R | grep "hello,world") && echo "True"
