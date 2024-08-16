#!/bin/bash
grep -q 'directory' /home/labex/project/environment.sh \
  && grep -q 'user' /home/labex/project/environment.sh \
  && grep -q 'used' /home/labex/project/environment.sh \
  && grep -q 'PATH' /home/labex/project/environment.sh \
  && grep -q 'MY_VARIABLE' /home/labex/project/environment.sh \
  && grep -q 'unset' /home/labex/project/environment.sh
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
