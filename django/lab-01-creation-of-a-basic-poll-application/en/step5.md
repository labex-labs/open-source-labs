# Write your first view

Let's write the first view. Open the file `polls/views.py` and put the following Python code in it:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the polls directory, create a file called `urls.py`. Your app directory should now look like:

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

In the `polls/urls.py` file include the following code:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

The next step is to point the root URLconf at the `polls.urls` module. In `mysite/urls.py`, add an import for `django.urls.include` and insert an `~django.urls.include` in the `urlpatterns` list, so you have:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

The `~django.urls.include` function allows referencing other URLconfs. Whenever Django encounters `~django.urls.include`, it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The idea behind `~django.urls.include` is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (`polls/urls.py`), they can be placed under "/polls/", or under "/fun_polls/", or under "/content/polls/", or any other path root, and the app will still work.

> When to use `~django.urls.include()`
> You should always use `include()` when you include other URL patterns. `admin.site.urls` is the only exception to this.

You have now wired an `index` view into the URLconf. Verify it's working with the following command:

```bash
python manage.py runserver 0.0.0.0:8080
```

Go to <http://<url>/polls/> in your browser, and you should see the text "_Hello, world. You're at the polls index._", which you defined in the `index` view.

![Django URLconf structure](../assets/20230907-13-51-48-aOKKfCBX.png)

The `~django.urls.path` function is passed four arguments, two required: `route` and `view`, and two optional: `kwargs`, and `name`. At this point, it's worth reviewing what these arguments are for.

## `~django.urls.path` argument: `route`

`route` is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in `urlpatterns` and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.

Patterns don't search GET and POST parameters, or the domain name. For example, in a request to `https://www.example.com/myapp/`, the URLconf will look for `myapp/`. In a request to `https://www.example.com/myapp/?page=3`, the URLconf will also look for `myapp/`.

## `~django.urls.path` argument: `view`

When Django finds a matching pattern, it calls the specified view function with an `~django.http.HttpRequest` object as the first argument and any "captured" values from the route as keyword arguments. We'll give an example of this in a bit.

## `~django.urls.path` argument: `kwargs`

Arbitrary keyword arguments can be passed in a dictionary to the target view. We aren't going to use this feature of Django in the tutorial.

## `~django.urls.path` argument: `name`

Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.
