# 编写一个最简表单

让我们更新上一个教程中的投票详情模板（`polls/detail.html`），使模板包含一个HTML `<form>` 元素：

```html+django
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

快速浏览一下：

- 上述模板为每个问题选项显示一个单选按钮。每个单选按钮的 `value` 是相关问题选项的ID。每个单选按钮的 `name` 是 `"choice"`。这意味着，当有人选择其中一个单选按钮并提交表单时，它将发送POST数据 `choice=#`，其中 `#` 是所选选项的ID。这是HTML表单的基本概念。
- 我们将表单的 `action` 设置为 `{% url 'polls:vote' question.id %}`，并将 `method="post"`。使用 `method="post"`（与 `method="get"` 相对）非常重要，因为提交此表单的行为将在服务器端更改数据。每当你创建一个会在服务器端更改数据的表单时，都要使用 `method="post"`。这个提示并非特定于Django；这是一般良好的Web开发实践。
- `forloop.counter` 表示 `for` 标签循环了多少次。
- 由于我们正在创建一个POST表单（可能会有修改数据的效果），我们需要担心跨站请求伪造。幸运的是，你不必过于担心，因为Django提供了一个有用的系统来防范它。简而言之，所有针对内部URL的POST表单都应该使用 `{% csrf_token %}<csrf_token>` 模板标签。

现在，让我们创建一个Django视图来处理提交的数据并对其进行处理。请记住，在《创建公共接口视图》中，我们为投票应用创建了一个URL配置，其中包括这一行：

```python
path("<int:question_id>/vote/", views.vote, name="vote"),
```

我们还创建了 `vote()` 函数的一个虚拟实现。让我们创建一个实际版本。将以下内容添加到 `polls/views.py`：

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from.models import Choice, Question


#...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # 重新显示问题投票表单。
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "你没有选择一个选项。",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理POST数据后，始终返回一个HttpResponseRedirect。这可以防止用户点击后退按钮时数据被重复提交。
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

这段代码包含了一些我们在本教程中尚未涉及的内容：

- `request.POST <django.http.HttpRequest.POST>` 是一个类似字典的对象，它允许你通过键名访问提交的数据。在这种情况下，`request.POST['choice']` 返回所选选项的ID，作为一个字符串。`request.POST <django.http.HttpRequest.POST>` 的值始终是字符串。

  请注意，Django还提供 `request.GET
<django.http.HttpRequest.GET>` 以相同的方式访问GET数据 —— 但我们在代码中明确使用 `request.POST
<django.http.HttpRequest.POST>`，以确保数据仅通过POST调用进行更改。

- 如果POST数据中没有提供 `choice`，`request.POST['choice']` 将引发 `KeyError`。上述代码检查 `KeyError`，如果没有给出 `choice`，则会显示带有错误消息的问题表单。

- 在增加选项计数后，代码返回一个 `~django.http.HttpResponseRedirect` 而不是普通的 `~django.http.HttpResponse`。`~django.http.HttpResponseRedirect` 接受一个参数：用户将被重定向到的URL（关于在这种情况下如何构造URL，请参见下一点）。

  正如上面的Python注释所指出的，在成功处理POST数据后，你应该始终返回一个 `~django.http.HttpResponseRedirect`。这个提示并非特定于Django；这是一般良好的Web开发实践。

- 在这个例子中，我们在 `~django.http.HttpResponseRedirect` 构造函数中使用了 `~django.urls.reverse` 函数。这个函数有助于避免在视图函数中硬编码URL。它被给予我们想要传递控制权的视图的名称以及指向该视图的URL模式的可变部分。在这种情况下，使用我们在《创建公共接口视图》中设置的URL配置，这个 `~django.urls.reverse` 调用将返回一个类似于这样的字符串：

      "/polls/3/results/"

  其中 `3` 是 `question.id` 的值。然后，这个重定向的URL将调用 `'results'` 视图来显示最终页面。

如《创建公共接口视图》中所述，`request` 是一个 `~django.http.HttpRequest` 对象。有关 `~django.http.HttpRequest` 对象的更多信息，请参阅 `请求和响应文档 </ref/request-response>`。

有人对一个问题投票后，`vote()` 视图会重定向到该问题的结果页面。让我们编写那个视图：

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
```

这几乎与《创建公共接口视图》中的 `detail()` 视图完全相同。唯一的区别是模板名称。我们稍后会解决这个冗余问题。

现在，创建一个 `polls/results.html` 模板：

```html+django
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">再次投票？</a>
```

现在，在浏览器中访问 `/polls/1/` 并对问题进行投票。你应该会看到一个结果页面，每次投票时都会更新。如果你在没有选择选项的情况下提交表单，你应该会看到错误消息。

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

![投票表单界面](../assets/20230908-10-37-07-p9ewKbe6.png)

**注意**：

我们的 `vote()` 视图代码确实有一个小问题。它首先从数据库中获取 `selected_choice` 对象，然后计算 `votes` 的新值，然后将其保存回数据库。如果你的网站的两个用户试图 _同时_ 投票，这可能会出错：对于 `votes`，会检索到相同的值，比如说42。然后，对于两个用户，都会计算并保存新值43，但预期值应该是44。

这被称为 _竞态条件_。如果你感兴趣，可以阅读 `使用f避免竞态条件` 来了解如何解决这个问题。
