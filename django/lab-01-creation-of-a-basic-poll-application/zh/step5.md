# 编写你的第一个视图

让我们编写第一个视图。打开文件 `polls/views.py`，并在其中放入以下 Python 代码：

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

这是 Django 中可能的最简单视图。要调用该视图，我们需要将其映射到一个 URL——为此我们需要一个 URL 配置（URLconf）。

要在 polls 目录中创建一个 URLconf，创建一个名为 `urls.py` 的文件。现在你的应用目录应该如下所示：

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

在 `polls/urls.py` 文件中包含以下代码：

```python
from django.urls import path

from. import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

下一步是将根 URLconf 指向 `polls.urls` 模块。在 `mysite/urls.py` 中，添加对 `django.urls.include` 的导入，并在 `urlpatterns` 列表中插入一个 `~django.urls.include`，这样你就有了：

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

`~django.urls.include` 函数允许引用其他 URLconf。每当 Django 遇到 `~django.urls.include` 时，它会切掉到该点为止匹配的 URL 的任何部分，并将剩余的字符串发送到包含的 URLconf 进行进一步处理。

`~django.urls.include` 背后的想法是使插入和播放 URL 变得容易。由于投票应用有自己的 URLconf（`polls/urls.py`），它们可以放在 "/polls/" 下，或 "/fun_polls/" 下，或 "/content/polls/" 下，或任何其他路径根目录下，应用仍然可以正常工作。

> 何时使用 `~django.urls.include()`
> 当你包含其他 URL 模式时，你应该始终使用 `include()`。`admin.site.urls` 是唯一的例外。

你现在已经将一个 `index` 视图连接到了 URLconf 中。使用以下命令验证它是否正常工作：

```bash
python manage.py runserver 0.0.0.0:8080
```

在浏览器中访问 <http://<url>/polls/>，你应该会看到你在 `index` 视图中定义的文本“_Hello, world. You're at the polls index._”。

![Django URLconf structure](../assets/20230907-13-51-48-aOKKfCBX.png)

`~django.urls.path` 函数传递四个参数，两个是必需的：`route` 和 `view`，两个是可选的：`kwargs` 和 `name`。此时，值得回顾一下这些参数的用途。

## `~django.urls.path` 参数：`route`

`route` 是一个包含 URL 模式的字符串。在处理请求时，Django 从 `urlpatterns` 中的第一个模式开始，沿着列表向下，将请求的 URL 与每个模式进行比较，直到找到一个匹配的模式。

模式不会搜索 GET 和 POST 参数，也不会搜索域名。例如，在对 `https://www.example.com/myapp/` 的请求中，URLconf 会查找 `myapp/`。在对 `https://www.example.com/myapp/?page=3` 的请求中，URLconf 也会查找 `myapp/`。

## `~django.urls.path` 参数：`view`

当 Django 找到一个匹配的模式时，它会使用一个 `~django.http.HttpRequest` 对象作为第一个参数，并将来自路由的任何“捕获”值作为关键字参数调用指定的视图函数。我们稍后会给出一个示例。

## `~django.urls.path` 参数：`kwargs`

任意关键字参数可以作为字典传递给目标视图。在本教程中我们不会使用 Django 的这个功能。

## `~django.urls.path` 参数：`name`

为你的 URL 命名可以让你在 Django 的其他地方，特别是在模板中明确地引用它。这个强大的功能允许你在只触及一个文件的情况下，对项目的 URL 模式进行全局更改。
