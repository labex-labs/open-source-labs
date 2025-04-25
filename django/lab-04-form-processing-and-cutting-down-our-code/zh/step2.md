# 使用通用视图：代码越少越好

`detail()`（来自《创建公共接口视图》）和 `results()` 视图非常简短 —— 而且，如上所述，存在冗余。显示投票列表的 `index()` 视图也类似。

这些视图代表了基本 Web 开发中的一种常见情况：根据 URL 中传递的参数从数据库获取数据，加载模板并返回渲染后的模板。由于这种情况非常常见，Django 提供了一个快捷方式，称为“通用视图”系统。

通用视图将常见模式进行了抽象，以至于你甚至不需要编写 Python 代码就能编写一个应用程序。

让我们将投票应用转换为使用通用视图系统，这样我们就可以删除大量我们自己编写的代码。我们需要采取几个步骤来进行转换。我们将：

1. 转换 URL 配置。
2. 删除一些旧的、不需要的视图。
3. 引入基于 Django 通用视图的新视图。

请继续阅读以了解详细信息。

> 为什么要打乱代码结构？

一般来说，在编写 Django 应用程序时，你会评估通用视图是否适合你的问题，并从一开始就使用它们，而不是在中途重构代码。但是本教程到目前为止有意专注于以“困难的方式”编写视图，以专注于核心概念。

在开始使用计算器之前，你应该先了解基本数学。

## 修改 URL 配置

首先，打开 `polls/urls.py` URL 配置并按如下方式进行更改：

```python
from django.urls import path

from. import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

请注意，第二个和第三个路径字符串中匹配模式的名称已从 `<question_id>` 更改为 `<pk>`。

## 修改视图

接下来，我们将删除旧的 `index`、`detail` 和 `results` 视图，并改用 Django 的通用视图。为此，打开 `polls/views.py` 文件并按如下方式进行更改：

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from.models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """返回最后五个已发布的问题。"""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
  ...  # 与上面相同，无需更改。
```

我们在这里使用了两个通用视图：`~django.views.generic.list.ListView` 和 `~django.views.generic.detail.DetailView`。这两个视图分别抽象了“显示对象列表”和“显示特定类型对象的详细页面”的概念。

- 每个通用视图都需要知道它将作用于哪个模型。这通过 `model` 属性提供。
- `~django.views.generic.detail.DetailView` 通用视图期望从 URL 捕获的主键值被称为 `"pk"`，因此我们将通用视图的 `question_id` 更改为 `pk`。

默认情况下，`~django.views.generic.detail.DetailView` 通用视图使用一个名为 `<应用名称>/<模型名称>_detail.html` 的模板。在我们的例子中，它将使用模板 `"polls/question_detail.html"`。`template_name` 属性用于告诉 Django 使用特定的模板名称，而不是自动生成的默认模板名称。我们还为 `results` 列表视图指定了 `template_name` —— 这确保了结果视图和详细视图在渲染时具有不同的外观，尽管它们在幕后都是 `~django.views.generic.detail.DetailView`。

同样，`~django.views.generic.list.ListView` 通用视图使用一个名为 `<应用名称>/<模型名称>_list.html` 的默认模板；我们使用 `template_name` 告诉 `~django.views.generic.list.ListView` 使用我们现有的 `"polls/index.html"` 模板。

在本教程的前面部分，模板被提供了一个上下文，其中包含 `question` 和 `latest_question_list` 上下文变量。对于 `DetailView`，`question` 变量会自动提供 —— 因为我们使用的是 Django 模型（`Question`），Django 能够为上下文变量确定一个合适的名称。然而，对于 `ListView`，自动生成的上下文变量是 `question_list`。为了覆盖这个变量，我们提供了 `context_object_name` 属性，指定我们想要使用 `latest_question_list` 代替。作为另一种方法，你可以更改模板以匹配新的默认上下文变量 —— 但告诉 Django 使用你想要的变量要容易得多。

运行服务器，并使用基于通用视图的新投票应用。
