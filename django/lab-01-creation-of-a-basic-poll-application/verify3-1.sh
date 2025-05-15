#!/bin/bash
cat ~/project/mysite/mysite/settings.py | grep "ALLOWED_HOSTS" | grep "*"
