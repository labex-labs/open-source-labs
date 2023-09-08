#!/bin/zsh
cd ~/project/mysite
python manage.py test polls | grep "Ran 10 tests"
python manage.py test polls | grep "OK"
