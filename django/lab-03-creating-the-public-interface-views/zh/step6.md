# 移除模板中的硬编码URL

请记住，当我们在 `polls/index.html` 模板中编写指向问题的链接时，该链接部分是硬编码的，如下所示：

```html+django
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

这种硬编码、紧密耦合的方法的问题在于，在有很多模板的项目中更改URL变得很有挑战性。但是，由于你在 `polls.urls` 模块的 `~django.urls.path` 函数中定义了 `name` 参数，你可以通过使用 `{% url %}` 模板标签来消除对URL配置中定义的特定URL路径的依赖：

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

其工作方式是通过查找 `polls.urls` 模块中指定的URL定义。你可以确切地看到下面定义了 “detail” 的URL名称的位置：

```python
# 被 {% url %} 模板标签调用的 'name' 值
path("<int:question_id>/", views.detail, name="detail"),
```

如果你想将投票详情视图的URL更改为其他内容，例如改为 `polls/specifics/12/`，而不是在模板中进行更改（或多个模板），你可以在 `polls/urls.py` 中进行更改：

> 你根本不需要更改模板。

```python
# 添加了单词'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
```
