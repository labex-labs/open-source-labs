#!/bin/zsh

test -z "$(docker ps -a | grep c1 | grep alpine)"
