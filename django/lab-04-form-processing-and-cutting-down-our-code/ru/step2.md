# Используйте общие представления: меньше кода - лучше

Представления `detail()` (из раздела **Создание представлений для общедоступного интерфейса**) и `results()` очень короткие — и, как упоминалось выше, избыточны. Аналогично выглядит представление `index()`, которое отображает список опросов.

Эти представления представляют собой общий случай базовой веб-разработки: получение данных из базы данных в соответствии с параметром, переданным в URL, загрузка шаблона и возврат отрендеренного шаблона. Поскольку это так часто встречается, Django предоставляет сокращение, называемое системой «общих представлений».

Общие представления абстрагируют общие шаблоны настолько, что вам даже не нужно писать Python-код для создания приложения.

Преобразуем наше приложение с опросами для использования системы общих представлений, чтобы можно было удалить кучу нашего собственного кода. Для этого нам придется предпринять несколько шагов:

1. Преобразовать URL-конфигурацию.
2. Удалить некоторые старые, не нужные представления.
3. Ввести новые представления на основе общих представлений Django.

Дальше вы найдете подробности.

> Почему перемешивать код?

一般来说，在编写 Django 应用程序时，您会评估通用视图是否适合您的问题，并从一开始就使用它们，而不是在中途重构代码。但本教程到目前为止有意专注于“艰难地”编写视图，以专注于核心概念。

在开始使用计算器之前，您应该先了解基本数学。

## Измените URL-конфигурацию

首先，打开 URL-конфигурацию `polls/urls.py` 并按如下方式进行更改：

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

请注意，第二个和第三个模式的路径字符串中匹配模式的名称已从 `<question_id>` 更改为 `<pk>`。

## Измените представления

接下来，我们将删除旧的 `index`、`detail` 和 `results` 视图，并改用 Django 的通用视图。为此，打开文件 `polls/views.py` 并按如下方式进行更改：

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
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
  ...  # то же, что и выше, изменения не требуются.
```

我们在这里使用了两个通用视图：`~django.views.generic.list.ListView` 和 `~django.views.generic.detail.DetailView`。相应地，这两个视图分别抽象了“显示对象列表”和“显示特定类型对象的详细页面”的概念。

- 每个通用视图都需要知道它将作用于哪个模型。这通过 `model` 属性提供。
- 通用视图 `~django.views.generic.detail.DetailView` 期望从 URL 捕获的主键值称为 `"pk"`，因此我们将通用视图的 `question_id` 更改为 `pk`。

默认情况下，通用视图 `~django.views.generic.detail.DetailView` 使用名为 `<应用名称>/<模型名称>_detail.html` 的模板。在我们的例子中，它将使用模板 `"polls/question_detail.html"`。`template_name` 属性用于告诉 Django 使用特定的模板名称，而不是自动生成的默认模板名称。我们还为结果列表视图指定了 `template_name` —— 这确保了结果视图和详细视图在渲染时具有不同的外观，尽管它们在幕后都是 `~django.views.generic.detail.DetailView`。

类似地，通用视图 `~django.views.generic.list.ListView` 使用默认模板 `<应用名称>/<模型名称>_list.html`；我们使用 `template_name` 告诉 `~django.views.generic.list.ListView` 使用我们现有的 `"polls/index.html"` 模板。

在本教程的前几部分中，模板已提供了一个上下文，其中包含 `question` 和 `latest_question_list` 上下文变量。对于 `DetailView`，`question` 变量会自动提供 —— 因为我们使用的是 Django 模型 (`Question`)，Django 能够为上下文变量确定合适的名称。但是，对于 `ListView`，自动生成的上下文变量是 `question_list`。为了覆盖此设置，我们提供了 `context_object_name` 属性，指定我们希望使用 `latest_question_list` 代替。作为另一种方法，您可以更改模板以匹配新的默认上下文变量 —— 但告诉 Django 使用您想要的变量要容易得多。

运行服务器，并使用基于通用视图的新投票应用程序。
