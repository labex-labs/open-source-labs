#!/bin/zsh
(cd /home/labex/project/git-playground && git show HEAD~1 | less -R | grep "+++ b/hello.txt
@@ -0,0 +1 @@
+hello,world" ) && echo "True"