# Raising a 404 error

Now, let's tackle the question detail view -- the page that displays the question text for a given poll. Here's the view:

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question


# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

The new concept here: The view raises the `~django.http.Http404` exception if a question with the requested ID doesn't exist.

We'll discuss what you could put in that `polls/detail.html` template a bit later, but if you'd like to quickly get the above example working, a file containing just:

```html+django
{{ question }}
```

will get you started for now.

## A shortcut: `~django.shortcuts.get_object_or_404`

It's a very common idiom to use `~django.db.models.query.QuerySet.get` and raise `~django.http.Http404` if the object doesn't exist. Django provides a shortcut. Here's the `detail()` view, rewritten:

```python
from django.shortcuts import get_object_or_404, render

from .models import Question


# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

The `~django.shortcuts.get_object_or_404` function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the `~django.db.models.query.QuerySet.get` function of the model's manager. It raises `~django.http.Http404` if the object doesn't exist.

Why do we use a helper function `~django.shortcuts.get_object_or_404` instead of automatically catching the `~django.core.exceptions.ObjectDoesNotExist` exceptions at a higher level, or having the model API raise `~django.http.Http404` instead of `~django.core.exceptions.ObjectDoesNotExist`?

Because that would couple the model layer to the view layer. One of the foremost design goals of Django is to maintain loose coupling. Some controlled coupling is introduced in the `django.shortcuts` module.

There's also a `~django.shortcuts.get_list_or_404` function, which works just as `~django.shortcuts.get_object_or_404` -- except using `~django.db.models.query.QuerySet.filter` instead of `~django.db.models.query.QuerySet.get`. It raises `~django.http.Http404` if the list is empty.
