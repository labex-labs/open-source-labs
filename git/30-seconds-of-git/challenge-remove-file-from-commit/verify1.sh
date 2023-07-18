#!/bin/zsh
 (cd /home/labex/project/git-playground && git show HEAD | less -R | grep "add git-playground.txt") && (cd /home/labex/project/git-playground && git show HEAD | less -R | grep "diff --git a/file1.txt b/file1.txt
deleted file mode 100644
index bfccc4a..0000000
--- a/file1.txt
+++ /dev/null") && echo "True"

