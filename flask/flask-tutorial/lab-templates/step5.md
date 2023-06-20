# Create the base template

Create a new file called `base.html` inside the `templates` directory and add the following code:

```html+jinja
<!doctype html>
<html>
<head>
    <title>{% block title %}Flask App{% endblock %}</title>
</head>
<body>
    <header>
        {% block header %}
        <h1>Flask App</h1>
        {% endblock %}
    </header>
    <section class="content">
        {% block content %}
        <p>Welcome to my Flask App!</p>
        {% endblock %}
    </section>
</body>
</html>
```
