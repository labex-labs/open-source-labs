# Создание базового макета

Нашим первым шагом будет создание базового макета, который будет использоваться для всех наших страниц. Этот базовый макет будет включать общие элементы нашего приложения, такие как панель навигации и заголовок страницы.

```html
<!-- flaskr/templates/base.html -->
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
    <li><span>{{ g.user['username'] }}</span></li>
    <li><a href="{{ url_for('auth.logout') }}">Выйти</a> {% else %}</li>

    <li><a href="{{ url_for('auth.register') }}">Зарегистрироваться</a></li>
    <li>
      <a href="{{ url_for('auth.login') }}">Войти</a>
      {% endif %}
    </li>
  </ul>
</nav>
<section class="content">
  <header>{% block header %}{% endblock %}</header>
  {% for message in get_flashed_messages() %}
  <div class="flash">{{ message }}</div>
  {% endfor %} {% block content %}{% endblock %}
</section>
```
