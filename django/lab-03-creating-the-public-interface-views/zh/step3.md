# 编写实际执行某些操作的视图

每个视图负责执行以下两件事之一：返回一个包含请求页面内容的 `~django.http.HttpResponse` 对象，或者引发一个异常，如 `~django.http.Http404`。其余的就由你决定了。

你的视图可以从数据库读取记录，也可以不读取。它可以使用诸如 Django 的模板系统 —— 或者第三方 Python 模板系统 —— 也可以不使用。它可以生成 PDF 文件、输出 XML、即时创建 ZIP 文件，使用任何你想要的 Python 库来做任何你想做的事情。

Django 所需要的只是那个 `~django.http.HttpResponse` 对象。或者一个异常。

为了方便起见，让我们使用 Django 自己的数据库 API，我们在教程 2 中介绍过。这是一个新的 `index()` 视图的尝试，它根据发布日期显示系统中最新的 5 个投票问题，用逗号分隔：

编辑 `polls/views.py` 文件并将其修改为如下所示：

```python
from django.http import HttpResponse

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# 其余的视图（detail、results、vote）保持不变
```

不过，这里有个问题：页面的设计在视图中是硬编码的。如果你想改变页面的外观，就必须编辑这段 Python 代码。所以，让我们使用 Django 的模板系统，通过创建一个视图可以使用的模板，将设计与 Python 分开。

首先，在你的 `polls` 目录中创建一个名为 `templates` 的目录。Django 会在那里寻找模板。

你的项目的 `TEMPLATES` 设置描述了 Django 将如何加载和渲染模板。默认的设置文件配置了一个 `DjangoTemplates` 后端，其 `APP_DIRS <TEMPLATES-APP_DIRS>` 选项设置为 `True`。按照惯例，`DjangoTemplates` 在每个 `INSTALLED_APPS` 中寻找一个名为“templates”的子目录。

在你刚刚创建的 `templates` 目录中，再创建一个名为 `polls` 的目录，然后在其中创建一个名为 `index.html` 的文件。换句话说，你的模板应该位于 `polls/templates/polls/index.html`。由于上述 `app_directories` 模板加载器的工作方式，你可以在 Django 中把这个模板引用为 `polls/index.html`。

## 模板命名空间

现在，我们 _也许_ 可以直接把模板放在 `polls/templates` 中（而不是再创建一个 `polls` 子目录），但这实际上是个坏主意。Django 会选择它找到的第一个名称匹配的模板，如果你在 _另一个_ 应用中有一个同名的模板，Django 将无法区分它们。

我们需要能够让 Django 找到正确的模板，而确保这一点的最佳方法是通过 _命名空间_ 它们。也就是说，把那些模板放在另一个以应用本身命名的目录中。

在那个模板中放入以下代码：

```html+django
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

注意：

为了使教程更简短，所有模板示例都使用不完整的 HTML。在你自己的项目中，你应该使用[完整的 HTML 文档](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document)。

现在让我们更新 `polls/views.py` 中的 `index` 视图以使用该模板：

```python
from django.http import HttpResponse
from django.template import loader

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

这段代码加载名为 `polls/index.html` 的模板，并向其传递一个上下文。上下文是一个将模板变量名映射到 Python 对象的字典。

再次运行服务器：

```bash
python manage.py runserver 0.0.0.0:8080
```

通过在浏览器中访问“/polls/”来加载页面，你应该会看到一个包含教程 2 中“What's up”问题的项目符号列表。该链接指向问题的详情页面。

![Django 投票索引页面](../assets/20230908-09-37-26-QMKEbUhb.png)

## 一个快捷方式：`~django.shortcuts.render`

加载模板、填充上下文并返回一个包含渲染后模板结果的 `~django.http.HttpResponse` 对象是一种非常常见的习惯用法。Django 提供了一个快捷方式。这是重写后的完整 `index()` 视图：

```python
from django.shortcuts import render

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

请注意，一旦我们在所有这些视图中都这样做了，我们就不再需要导入 `~django.template.loader` 和 `~django.http.HttpResponse`（如果你仍然有 `detail`、`results` 和 `vote` 的存根方法，你可能还需要保留 `HttpResponse`）。

`~django.shortcuts.render` 函数将请求对象作为其第一个参数，模板名称作为其第二个参数，并将字典作为其可选的第三个参数。它返回一个使用给定上下文渲染的给定模板的 `~django.http.HttpResponse` 对象。
