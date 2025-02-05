# 创建基础布局

我们的第一步是创建一个将用于所有页面的基础布局。这个基础布局将包括我们应用程序的常见元素，如导航栏和页面标题。

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
    <li><a href="{{ url_for('auth.logout') }}">退出登录</a> {% else %}</li>

    <li><a href="{{ url_for('auth.register') }}">注册</a></li>
    <li>
      <a href="{{ url_for('auth.login') }}">登录</a>
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
