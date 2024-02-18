#!/bin/zsh
cd /tmp
wget https://static.rust-lang.org/rustup/rustup-init.sh
sudo chmod +x rustup-init.sh
./rustup-init.sh -y
# Initialize .zsh_history
touch /home/labex/.zsh_history
