# Register Template

Next, we will create a template for the registration page. This template will extend our base layout and fill in the specific content for this page.

```html
<!-- flaskr/templates/auth/register.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Register{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Username</label>
  <input name="username" id="username" required />
  <label for="password">Password</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Register" />
</form>
{% endblock %}
```
