# 注册模板

接下来，我们将为注册页面创建一个模板。这个模板将扩展我们的基础布局，并填充此页面的特定内容。

```html
<!-- flaskr/templates/auth/register.html -->
{% extends 'base.html' %} {% block header %}
<h1>{% block title %}注册{% endblock %}</h1>
{% endblock %} {% block content %}
<form method="post">
  <label for="username">用户名</label>
  <input name="username" id="username" required />
  <label for="password">密码</label>
  <input type="password" name="password" id="password" required />
  <input type="submit" value="注册" />
</form>
{% endblock %}
```
