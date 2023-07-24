#!/bin/zsh

cd ~/project
git diff | grep 'option_context'
git diff | grep 'get_option'
