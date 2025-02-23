# Erstellung des Basislayouts

Unser erster Schritt besteht darin, ein Basislayout zu erstellen, das für alle unsere Seiten verwendet werden soll. Dieses Basislayout wird die gemeinsamen Elemente unserer Anwendung wie die Navigationsleiste und den Seitentitel enthalten.

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
    <li><a href="{{ url_for('auth.logout') }}">Abmelden</a> {% else %}</li>

    <li><a href="{{ url_for('auth.register') }}">Registrieren</a></li>
    <li>
      <a href="{{ url_for('auth.login') }}">Anmelden</a>
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
