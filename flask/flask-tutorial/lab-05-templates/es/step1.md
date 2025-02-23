# Creando la Plantilla Base

Nuestro primer paso es crear una plantilla base que se utilizará para todas nuestras páginas. Esta plantilla base incluirá los elementos comunes de nuestra aplicación, como la barra de navegación y el título de la página.

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
    <li><a href="{{ url_for('auth.logout') }}">Cerrar Sesión</a> {% else %}</li>

    <li><a href="{{ url_for('auth.register') }}">Registrarse</a></li>
    <li>
      <a href="{{ url_for('auth.login') }}">Iniciar Sesión</a>
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
