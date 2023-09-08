#!/bin/zsh
cd ~/project/mysite
python manage.py test polls | grep "Ran 3 tests"
python manage.py test polls | grep "OK"
