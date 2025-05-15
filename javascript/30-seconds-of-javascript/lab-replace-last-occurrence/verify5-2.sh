#!/bin/bash
test -f /home/labex/project/replace-last/app.js && grep 'require' /home/labex/project/replace-last/app.js && echo 'success'
