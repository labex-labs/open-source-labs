# Flask Template Lab

## Introduction

In this lab, we will learn how to create and use templates in Flask. Templates are a crucial part of web applications. They allow us to generate dynamic HTML pages that can display different data each time they are loaded. We'll be using the Jinja2 template engine that comes bundled with Flask.

## Steps

### Step 1: Creating the Base Layout

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

### Step 2: Register Template

Next, we will create a template for the registration page. This template will extend our base layout and fill in the specific content for this page.

```html
<!-- flaskr/templates/auth/register.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Register{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Username</label>
  <input name="username" id="username" required />
  <label for="password">Password</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Register" />
</form>
{% endblock %}
```

### Step 3: Login Template

Similarly, we will create a template for the login page. This template will also extend our base layout and fill in the specific content for this page.

```html
<!-- flaskr/templates/auth/login.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">Username</label>
  <input name="username" id="username" required />
  <label for="password">Password</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="Log In" />
</form>
{% endblock %}
```

## Summary

In this lab, we learned how to create and use templates in Flask. We created a base layout that includes the common elements of our application, and then we created specific templates for the registration and login pages that extend this base layout and fill in their specific content. This allows us to keep our code DRY (Don't Repeat Yourself), making it more maintainable and less prone to errors.
