#!/bin/bash
cd ~/project/mysite
python manage.py test polls | grep "3"
