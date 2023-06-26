#!/bin/zsh

test -z "$(docker ps -a | grep c2 | grep img1)"