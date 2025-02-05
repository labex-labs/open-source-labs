# 使用模板系统

回到我们投票应用的 `detail()` 视图。给定上下文变量 `question`，`polls/detail.html` 模板可能如下所示：

```html+django
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

模板系统使用点号查找语法来访问变量属性。在 `{{ question.question_text }}` 的示例中，首先Django在对象 `question` 上进行字典查找。如果失败，它会尝试进行属性查找 —— 在这种情况下是可行的。如果属性查找失败，它会尝试进行列表索引查找。

方法调用发生在 `{% for %}<for>` 循环中：`question.choice_set.all` 被解释为Python代码 `question.choice_set.all()`，它返回一个 `Choice` 对象的可迭代对象，适用于 `{% for %}<for>` 标签。
