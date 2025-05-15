#!/bin/bash
(cd /home/labex/project/my_project && git status | grep "On branch") && echo "True"
