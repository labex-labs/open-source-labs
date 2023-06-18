#!/bin/zsh
<<<<<<< HEAD
(cd /home/labex/project/git-playground && ll | grep "file2.txt") && echo "True"
=======
(cat ~/.zsh_history | grep -v grep | grep "git checkout") && (cat ~/.zsh_history | grep -v grep | grep "rm example.txt") && (cd /home/labex/project/git-playground && git status | grep 'Changes to be committed:
  (use "git restore --staged <file>..." to unstage)') && echo "True"

>>>>>>> 1fec746dcce4ca206f17285ebdc2abe98e31a364
