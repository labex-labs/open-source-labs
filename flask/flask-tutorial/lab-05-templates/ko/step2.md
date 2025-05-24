# 등록 템플릿

다음으로, 등록 페이지에 대한 템플릿을 생성합니다. 이 템플릿은 기본 레이아웃을 확장하고 이 페이지에 대한 특정 콘텐츠를 채웁니다.

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
