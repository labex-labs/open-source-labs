#!/bin/bash
cat ~/project/mysite/polls/views.py | grep "class ResultsView"
cat ~/project/mysite/polls/urls.py | grep "views.IndexView"
