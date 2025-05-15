#!/bin/bash

cd ~/project

curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

sudo apt update
sudo apt install -y nodejs

unzip demo.zip && mv demo/* ./ && rm -rf demo*
