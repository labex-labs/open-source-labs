#!/bin/bash
grep -q 'echo "Home directory: $HOME"' /home/labex/project/environment.sh \
  && grep -q 'echo "Current user: $USER"' /home/labex/project/environment.sh \
  && grep -q 'echo "Shell being used: $SHELL"' /home/labex/project/environment.sh \
  && grep -q 'echo "Current PATH: $PATH"' /home/labex/project/environment.sh \
  && grep -q 'export MY_VARIABLE="Hello from my variable"' /home/labex/project/environment.sh \
  && grep -q 'unset MY_VARIABLE' /home/labex/project/environment.sh
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
