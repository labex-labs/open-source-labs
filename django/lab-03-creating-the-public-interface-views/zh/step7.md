# 为URL名称添加命名空间

本教程项目只有一个应用，即 “polls”。在实际的Django项目中，可能会有五个、十个、二十个或更多的应用。Django如何区分它们之间的URL名称呢？例如，“polls” 应用有一个 “detail” 视图，同一个项目中用于博客的应用可能也有。如何确保在使用 `{% url %}` 模板标签时，Django知道为某个URL创建哪个应用的视图呢？

答案是为你的URL配置添加命名空间。在 `polls/urls.py` 文件中，继续添加一个 `app_name` 来设置应用命名空间：

```python
from django.urls import path

from. import views

app_name = "polls"
urlpatterns = [
    # 例如：/polls/
    path("", views.index, name="index"),
    # 例如：/polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # 例如：/polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # 例如：/polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

现在将你的 `polls/index.html` 模板从：

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

改为指向带有命名空间的详情视图：

```html+django
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

![URL命名空间示例](../assets/20230908-09-58-22-qkl9l0DT.png)

当你对编写视图感到得心应手时，请阅读 **表单处理与简化代码** 来学习表单处理和通用视图的基础知识。
