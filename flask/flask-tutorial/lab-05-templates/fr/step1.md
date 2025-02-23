# Création de la mise en page de base

Notre première étape consiste à créer une mise en page de base qui sera utilisée pour toutes nos pages. Cette mise en page de base inclura les éléments communs de notre application, comme la barre de navigation et le titre de la page.

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
    <li><a href="{{ url_for('auth.logout') }}">Déconnexion</a> {% else %}</li>

    <li><a href="{{ url_for('auth.register') }}">Inscription</a></li>
    <li>
      <a href="{{ url_for('auth.login') }}">Connexion</a>
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
