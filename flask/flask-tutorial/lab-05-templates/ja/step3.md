# ログインテンプレート

同様に、ログインページ用のテンプレートを作成します。このテンプレートも基本レイアウトを拡張し、このページの特定のコンテンツを埋めます。

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
