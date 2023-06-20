# Creating the Base Layout

Our first step is to create a base layout that will be used for all our pages. This base layout will include the common elements of our application like the navigation bar and the page title.

```html
<!-- flaskr/templates/base.html -->
<!DOCTYPE html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
    <li><span>{{ g.user['username'] }}</span></li>
    <li><a href="{{ url_for('auth.logout') }}">Log Out</a> {% else %}</li>

    <li><a href="{{ url_for('auth.register') }}">Register</a></li>
    <li>
      <a href="{{ url_for('auth.login') }}">Log In</a>
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
