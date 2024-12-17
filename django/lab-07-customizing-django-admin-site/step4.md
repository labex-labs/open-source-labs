# Customize the admin look and feel

Clearly, having "Django administration" at the top of each admin page is ridiculous. It's just placeholder text.

You can change it, though, using Django's template system. The Django admin is powered by Django itself, and its interfaces use Django's own template system.

## Customizing your _project's_ templates

Create a `templates` directory in your project directory (the one that contains `manage.py`). Templates can live anywhere on your filesystem that Django can access. (Django runs as whatever user your server runs.) However, keeping your templates within the project is a good convention to follow.

Open your settings file (`mysite/settings.py`, remember) and add a `DIRS <TEMPLATES-DIRS>` option in the `TEMPLATES` setting:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

`DIRS <TEMPLATES-DIRS>` is a list of filesystem directories to check when loading Django templates; it's a search path.

## Organizing templates

Just like the static files, we _could_ have all our templates together, in one big templates directory, and it would work perfectly well. However, templates that belong to a particular application should be placed in that application's template directory (e.g. `polls/templates`) rather than the project's (`templates`). We'll discuss in more detail in the `reusable apps tutorial </intro/reusable-apps>` _why_ we do this.

Now create a directory called `admin` inside `templates`, and copy the template `admin/base_site.html` from within the default Django admin template directory in the source code of Django itself (`django/contrib/admin/templates`) into that directory.

## Where are the Django source files?

If you have difficulty finding where the Django source files are located on your system, run the following command:

```bash
python -c "import django; print(django.__path__)"
```

```plaintext
['/home/labex/.local/lib/python3.10/site-packages/django']
```

Then, edit the file and replace `{{ site_header|default:_('Django administration') }}` (including the curly braces) with your own site's name as you see fit. You should end up with a section of code like:

```html+django
{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a><div>
{% endblock %}
```

We use this approach to teach you how to override templates. In an actual project, you would probably use the `django.contrib.admin.AdminSite.site_header` attribute to more easily make this particular customization.

This template file contains lots of text like `{% block branding %}` and `{{ title }}`. The `{%` and `{{` tags are part of Django's template language. When Django renders `admin/base_site.html`, this template language will be evaluated to produce the final HTML page, just like we saw in `**Creating the Public Interface Views**`.

Note that any of Django's default admin templates can be overridden. To override a template, do the same thing you did with `base_site.html` -- copy it from the default directory into your custom directory, and make changes.

## Customizing your _application's_ templates

Astute readers will ask: But if `DIRS <TEMPLATES-DIRS>` was empty by default, how was Django finding the default admin templates? The answer is that, since `APP_DIRS <TEMPLATES-APP_DIRS>` is set to `True`, Django automatically looks for a `templates/` subdirectory within each application package, for use as a fallback (don't forget that `django.contrib.admin` is an application).

Our poll application is not very complex and doesn't need custom admin templates. But if it grew more sophisticated and required modification of Django's standard admin templates for some of its functionality, it would be more sensible to modify the _application's_ templates, rather than those in the _project_. That way, you could include the polls application in any new project and be assured that it would find the custom templates it needed.

See the `template loading documentation <template-loading>` for more information about how Django finds its templates.
