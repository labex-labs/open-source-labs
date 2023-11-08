#!/bin/zsh
cd ~/project

wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash

nvm install 16.14

nvm use 16.14

nvm alias default 16.14