#!/bin/bash
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground.git
cd /home/labex/project/git-playground
git fetch origin
git checkout -b feature-branch
