# Create a child template

Create a new file called `child.html` inside the `templates` directory and add the following code:

```html+jinja
{% extends 'base.html' %}

{% block header %}
    <h1>Child Template</h1>
{% endblock %}

{% block content %}
    <p>This is the content of the child template.</p>
{% endblock %}
```
