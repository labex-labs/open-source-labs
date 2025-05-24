# Template de Login

Da mesma forma, criaremos um template para a página de login. Este template também estenderá nosso layout base e preencherá o conteúdo específico para esta página.

```html
<!-- flaskr/templates/auth/login.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Username</label>
  <input name="username" id="username" required />
  <label for="password">Password</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Log In" />
</form>
{% endblock %}
```
