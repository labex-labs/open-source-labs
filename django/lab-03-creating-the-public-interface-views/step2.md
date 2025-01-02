# Writing more views

Now let's add a few more views to `polls/views.py`. These views are slightly different, because they take an argument:

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

Wire these new views into the `polls.urls` module by adding the following `~django.urls.path` calls:

Edit the `polls/urls.py` file and add the following lines:

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Now, run the server again:

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

Swith to **Web 8080** tab, at `/polls/34/`. It'll run the `detail()` method and display whatever ID you provide in the URL. Try `/polls/34/results/` and `/polls/34/vote/` too -- these will display the placeholder results and voting pages.

![Django URL routing diagram](./assets/20230908-09-30-06-2n54ROPe.png)

When somebody requests a page from your website -- say, `/polls/34/`, Django will load the `mysite.urls` Python module because it's pointed to by the `ROOT_URLCONF` setting. It finds the variable named `urlpatterns` and traverses the patterns in order. After finding the match at `'polls/'`, it strips off the matching text (`"polls/"`) and sends the remaining text --`"34/"` -- to the 'polls.urls' URLconf for further processing. There it matches `'<int:question_id>/'`, resulting in a call to the `detail()` view like so:

```python
detail(request=<HttpRequest object>, question_id=34)
```

The `question_id=34` part comes from `<int:question_id>`. Using angle brackets "captures" part of the URL and sends it as a keyword argument to the view function. The `question_id` part of the string defines the name that will be used to identify the matched pattern, and the `int` part is a converter that determines what patterns should match this part of the URL path. The colon (`:`) separates the converter and pattern name.
