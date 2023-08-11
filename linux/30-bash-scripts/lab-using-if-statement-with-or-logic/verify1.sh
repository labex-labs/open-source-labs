#!/bin/zsh
cd /home/labex/project
echo "15" | bash if_with_OR.sh | grep "won"
echo "115" | bash if_with_OR.sh | grep "lost"