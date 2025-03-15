#!/bin/zsh

# Check if the user has run the exec example
if ! cat ~/.zsh_history | grep -q "exec"; then
  echo "Please run the exec examples as shown in Step 1."
  exit 1
fi

exit 0
