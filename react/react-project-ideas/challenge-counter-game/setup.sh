#!/bin/zsh

cd ~/project

curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

sudo apt-get install -y nodejs

unzip project.zip && mv project/* ./ && rm -rf project*