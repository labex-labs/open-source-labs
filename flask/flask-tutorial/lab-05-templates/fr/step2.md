# Modèle d'inscription

Ensuite, nous allons créer un modèle pour la page d'inscription. Ce modèle étendra notre mise en page de base et complètera le contenu spécifique de cette page.

```html
<!-- flaskr/templates/auth/register.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Inscription{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Nom d'utilisateur</label>
  <input name="username" id="username" required />
  <label for="password">Mot de passe</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Inscrire" />
</form>
{% endblock %}
```
