#!/bin/bash

# Check if the user has examined the source code of namedtuple
if ! cat ~/.zsh_history | grep -q "inspect.getsource"; then
  echo "Please examine the source code of namedtuple using inspect.getsource()."
  exit 1
fi

exit 0
