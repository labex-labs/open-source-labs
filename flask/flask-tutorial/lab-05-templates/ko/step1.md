# 기본 레이아웃 생성

첫 번째 단계는 모든 페이지에 사용될 기본 레이아웃을 만드는 것입니다. 이 기본 레이아웃에는 탐색 모음 및 페이지 제목과 같이 애플리케이션의 공통 요소가 포함됩니다.

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
