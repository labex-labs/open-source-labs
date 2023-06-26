#!/bin/zsh

cat ~/.zsh_history | grep docker | grep run | grep c3 | grep "-d" | grep "-v"
