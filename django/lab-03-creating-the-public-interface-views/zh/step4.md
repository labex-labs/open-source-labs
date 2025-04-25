# 引发 404 错误

现在，让我们来处理问题详情视图 —— 即显示给定投票的问题文本的页面。以下是该视图：

```python
from django.http import Http404
from django.shortcuts import render

from.models import Question


#...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("问题不存在")
    return render(request, "polls/detail.html", {"question": question})
```

这里的新概念是：如果不存在具有请求 ID 的问题，视图将引发 `~django.http.Http404` 异常。

稍后我们将讨论可以在 `polls/detail.html` 模板中放入什么内容，但如果你想快速使上述示例生效，一个只包含以下内容的文件：

```html+django
{{ question }}
```

现在就可以让你开始了。

## 一个快捷方式：`~django.shortcuts.get_object_or_404`

使用 `~django.db.models.query.QuerySet.get` 并在对象不存在时引发 `~django.http.Http404` 是一种非常常见的习惯用法。Django 提供了一个快捷方式。以下是重写后的 `detail()` 视图：

```python
from django.shortcuts import get_object_or_404, render

from.models import Question


#...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

`~django.shortcuts.get_object_or_404` 函数将一个 Django 模型作为其第一个参数，并接受任意数量的关键字参数，它将这些参数传递给模型管理器的 `~django.db.models.query.QuerySet.get` 函数。如果对象不存在，它将引发 `~django.http.Http404`。

为什么我们使用辅助函数 `~django.shortcuts.get_object_or_404`，而不是在更高层次自动捕获 `~django.core.exceptions.ObjectDoesNotExist` 异常，或者让模型 API 引发 `~django.http.Http404` 而不是 `~django.core.exceptions.ObjectDoesNotExist` 呢？

因为那样会将模型层与视图层耦合在一起。Django 最重要的设计目标之一是保持松散耦合。在 `django.shortcuts` 模块中引入了一些受控的耦合。

还有一个 `~django.shortcuts.get_list_or_404` 函数，它的工作方式与 `~django.shortcuts.get_object_or_404` 相同 —— 只是使用 `~django.db.models.query.QuerySet.filter` 而不是 `~django.db.models.query.QuerySet.get`。如果列表为空，它将引发 `~django.http.Http404`。
