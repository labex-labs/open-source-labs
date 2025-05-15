#!/bin/bash

cat ~/.zsh_history | grep -v grep | grep "weeks ago" && echo "True"
