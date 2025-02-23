# Шаблон регистрации

Далее мы создадим шаблон для страницы регистрации. Этот шаблон будет расширять наш базовый макет и заполнять специфический контент для этой страницы.

```html
<!-- flaskr/templates/auth/register.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Регистрация{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Имя пользователя</label>
  <input name="username" id="username" required />
  <label for="password">Пароль</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Зарегистрироваться" />
</form>
{% endblock %}
```
