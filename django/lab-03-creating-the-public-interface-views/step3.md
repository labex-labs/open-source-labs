# Write views that actually do something

Each view is responsible for doing one of two things: returning an `~django.http.HttpResponse` object containing the content for the requested page, or raising an exception such as `~django.http.Http404`. The rest is up to you.

Your view can read records from a database, or not. It can use a template system such as Django's -- or a third-party Python template system -- or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want.

All Django wants is that `~django.http.HttpResponse`. Or an exception.

Because it's convenient, let's use Django's own database API, which we covered in Tutorial 2. Here's one stab at a new `index()` view, which displays the latest 5 poll questions in the system, separated by commas, according to publication date:

Edit the `polls/views.py` file and change it to look like this:

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
```

There's a problem here, though: the page's design is hard-coded in the view. If you want to change the way the page looks, you'll have to edit this Python code. So let's use Django's template system to separate the design from Python by creating a template that the view can use.

First, create a directory called `templates` in your `polls` directory. Django will look for templates in there.

Your project's `TEMPLATES` setting describes how Django will load and render templates. The default settings file configures a `DjangoTemplates` backend whose `APP_DIRS <TEMPLATES-APP_DIRS>` option is set to `True`. By convention `DjangoTemplates` looks for a "templates" subdirectory in each of the `INSTALLED_APPS`.

Within the `templates` directory you have just created, create another directory called `polls`, and within that create a file called `index.html`. In other words, your template should be at `polls/templates/polls/index.html`. Because of how the `app_directories` template loader works as described above, you can refer to this template within Django as `polls/index.html`.

## Template namespacing

Now we _might_ be able to get away with putting our templates directly in `polls/templates` (rather than creating another `polls` subdirectory), but it would actually be a bad idea. Django will choose the first template it finds whose name matches, and if you had a template with the same name in a _different_ application, Django would be unable to distinguish between them.

We need to be able to point Django at the right one, and the best way to ensure this is by _namespacing_ them. That is, by putting those templates inside _another_ directory named for the application itself.

Put the following code in that template:

```html+django
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Note:

To make the tutorial shorter, all template examples use incomplete HTML. In your own projects you should use [complete HTML documents](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document).

Now let's update our `index` view in `polls/views.py` to use the template:

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

That code loads the template called `polls/index.html` and passes it a context. The context is a dictionary mapping template variable names to Python objects.

Run server again:

```bash
python manage.py runserver 0.0.0.0:8080
```

Load the page by pointing your browser at "/polls/", and you should see a bulleted-list containing the "What's up" question from Tutorial 2. The link points to the question's detail page.

![Alt text](./assets/20230908-09-37-26-QMKEbUhb.png)

### A shortcut: `~django.shortcuts.render`

It's a very common idiom to load a template, fill a context and return an `~django.http.HttpResponse` object with the result of the rendered template. Django provides a shortcut. Here's the full `index()` view, rewritten:

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

Note that once we've done this in all these views, we no longer need to import `~django.template.loader` and `~django.http.HttpResponse` (you'll want to keep `HttpResponse` if you still have the stub methods for `detail`, `results`, and `vote`).

The `~django.shortcuts.render` function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an `~django.http.HttpResponse` object of the given template rendered with the given context.
