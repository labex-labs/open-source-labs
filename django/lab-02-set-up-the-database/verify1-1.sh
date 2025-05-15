#!/bin/bash
cd ~/project/mysite
python manage.py migrate | grep "No migrations to apply"
