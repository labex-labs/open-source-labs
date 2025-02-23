# Anmeldevorlage

Ähnlich werden wir eine Vorlage für die Anmeldeseite erstellen. Diese Vorlage wird ebenfalls unser Basislayout erweitern und den spezifischen Inhalt für diese Seite einfügen.

```html
<!-- flaskr/templates/auth/login.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Anmelden{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Benutzername</label>
  <input name="username" id="username" required />
  <label for="password">Passwort</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Anmelden" />
</form>
{% endblock %}
```
