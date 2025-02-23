# Plantilla de Registro

A continuación, crearemos una plantilla para la página de registro. Esta plantilla extenderá nuestra plantilla base y llenará el contenido específico de esta página.

```html
<!-- flaskr/templates/auth/register.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Registrarse{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Nombre de usuario</label>
  <input name="username" id="username" required />
  <label for="password">Contraseña</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Registrarse" />
</form>
{% endblock %}
```
