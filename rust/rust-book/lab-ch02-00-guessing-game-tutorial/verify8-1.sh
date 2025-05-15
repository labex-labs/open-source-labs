#!/bin/bash

cat ~/.zsh_history | grep "cargo run"
cd ~/project/guessing_game && echo 5 | cargo run | grep "5"
