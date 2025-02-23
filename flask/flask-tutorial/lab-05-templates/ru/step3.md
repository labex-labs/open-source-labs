# Шаблон входа

Аналогично мы создадим шаблон для страницы входа. Этот шаблон также будет расширять наш базовый макет и заполнять специфический контент для этой страницы.

```html
<!-- flaskr/templates/auth/login.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Войти{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Имя пользователя</label>
  <input name="username" id="username" required />
  <label for="password">Пароль</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Войти" />
</form>
{% endblock %}
```
