# Overview

A view is a "type" of web page in your Django application that generally serves a specific function and has a specific template. For example, in a blog application, you might have the following views:

- Blog homepage -- displays the latest few entries.
- Entry "detail" page -- permalink page for a single entry.
- Year-based archive page -- displays all months with entries in the given year.
- Month-based archive page -- displays all days with entries in the given month.
- Day-based archive page -- displays all entries in the given day.
- Comment action -- handles posting comments to a given entry.

In our poll application, we'll have the following four views:

- Question "index" page -- displays the latest few questions.
- Question "detail" page -- displays a question text, with no results but with a form to vote.
- Question "results" page -- displays results for a particular question.
- Vote action -- handles voting for a particular choice in a particular question.

In Django, web pages and other content are delivered by views. Each view is represented by a Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that's requested (to be precise, the part of the URL after the domain name).

Now in your time on the web you may have come across such beauties as `ME2/Sites/dirmod.htm?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B`. You will be pleased to know that Django allows us much more elegant _URL patterns_ than that.

A URL pattern is the general form of a URL - for example: `/newsarchive/<year>/<month>/`.

To get from a URL to a view, Django uses what are known as 'URLconfs'. A URLconf maps URL patterns to views.

This tutorial provides basic instruction in the use of URLconfs, and you can refer to `/topics/http/urls` for more information.
