# Plantilla de Inicio de Sesión

De manera similar, crearemos una plantilla para la página de inicio de sesión. Esta plantilla también extenderá nuestra plantilla base y llenará el contenido específico de esta página.

```html
<!-- flaskr/templates/auth/login.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Iniciar Sesión{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Nombre de usuario</label>
  <input name="username" id="username" required />
  <label for="password">Contraseña</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Iniciar Sesión" />
</form>
{% endblock %}
```
