# 测试视图

投票应用程序相当随意：它会发布任何问题，包括那些 `pub_date` 字段在未来的问题。我们应该改进这一点。将 `pub_date` 设置为未来的时间应该意味着该问题在那一刻发布，但在此之前不可见。

## 对视图进行测试

当我们修复上述漏洞时，我们先编写了测试，然后编写了修复代码。实际上，这是测试驱动开发的一个例子，但我们按什么顺序进行这项工作并不重要。

在我们的第一个测试中，我们密切关注了代码的内部行为。对于这个测试，我们想检查它在用户通过网页浏览器体验时的行为。

在我们尝试修复任何问题之前，让我们先看看我们可以使用的工具。

## Django 测试客户端

Django 提供了一个测试 `~django.test.Client`，用于在视图级别模拟用户与代码的交互。我们可以在 `tests.py` 中使用它，甚至在 `shell` 中也可以。

我们将再次从 `shell` 开始，在那里我们需要做一些在 `tests.py` 中不需要做的事情。首先是在 `shell` 中设置测试环境：

```bash
python manage.py shell
```

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

`~django.test.utils.setup_test_environment` 安装了一个模板渲染器，这将允许我们检查响应上的一些额外属性，例如 `response.context`，否则这些属性是不可用的。请注意，此方法 _不会_ 设置测试数据库，因此以下操作将针对现有数据库运行，并且输出可能会因你已经创建的问题而略有不同。如果你的 `settings.py` 中的 `TIME_ZONE` 不正确，你可能会得到意外的结果。如果你不记得之前设置过它，请在继续之前检查一下。

接下来，我们需要导入测试客户端类（稍后在 `tests.py` 中，我们将使用 `django.test.TestCase` 类，它自带了自己的客户端，所以这里不需要）：

```python
>>> from django.test import Client
>>> # 创建一个供我们使用的客户端实例
>>> client = Client()
```

准备好之后，我们可以让客户端为我们做一些工作：

```python
>>> # 从'/'获取响应
>>> response = client.get("/")
Not Found: /
>>> # 我们应该从那个地址得到一个404；如果你看到的是
>>> # "Invalid HTTP_HOST header" 错误和一个400响应，你可能
>>> # 省略了前面描述的 setup_test_environment() 调用。
>>> response.status_code
404
>>> # 另一方面，我们应该期望在'/polls/'找到一些东西
>>> # 我们将使用'reverse()'而不是硬编码的URL
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
```

## 改进我们的视图

投票列表显示了尚未发布的投票（即那些 `pub_date` 在未来的投票）。让我们修复这个问题。

在《表单处理与精简代码》中，我们引入了一个基于 `~django.views.generic.list.ListView` 的类视图：

```python
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """返回最后五个已发布的问题。"""
        return Question.objects.order_by("-pub_date")[:5]
```

我们需要修改 `get_queryset()` 方法，并更改它，以便它还通过与 `timezone.now()` 进行比较来检查日期。首先，我们需要添加一个导入：

```python
from django.utils import timezone
```

然后我们必须像这样修改 `get_queryset` 方法：

```python
def get_queryset(self):
    """
    返回最后五个已发布的问题（不包括那些设置为在未来发布的问题）。
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
```

`Question.objects.filter(pub_date__lte=timezone.now())` 返回一个查询集，其中包含 `pub_date` 小于或等于（即早于或等于）`timezone.now` 的 `Question`。

## 测试我们的新视图

现在你可以通过启动 `runserver`，在浏览器中加载网站，创建过去和未来日期的 `Question`，并检查是否只列出了已发布的问题，来确保它按预期运行。你不想每次进行任何可能影响此功能的更改时都必须这样做——所以让我们也基于上面的 `shell` 会话创建一个测试。

在 `polls/tests.py` 中添加以下内容：

```python
from django.urls import reverse
```

我们还将创建一个快捷函数来创建问题以及一个新的测试类：

```python
def create_question(question_text, days):
    """
    使用给定的 `question_text` 创建一个问题，并将其发布时间设置为从现在起偏移给定的 `天数`（过去发布的问题为负数，尚未发布的问题为正数）。
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        如果没有问题存在，则显示适当的消息。
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        过去发布时间的问题显示在索引页面上。
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        未来发布时间的问题不在索引页面上显示。
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        即使同时存在过去和未来的问题，也只显示过去的问题。
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        问题索引页面可能会显示多个问题。
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )
```

让我们更仔细地看看其中一些测试。

首先是一个问题快捷函数 `create_question`，用于减少创建问题过程中的重复操作。

`test_no_questions` 不创建任何问题，但检查消息：“No polls are available.” 并验证 `latest_question_list` 为空。请注意，`django.test.TestCase` 类提供了一些额外的断言方法。在这些示例中，我们使用了 `~django.test.SimpleTestCase.assertContains()` 和 `~django.test.TransactionTestCase.assertQuerySetEqual()`。

在 `test_past_question` 中，我们创建一个问题并验证它出现在列表中。

在 `test_future_question` 中，我们创建一个 `pub_date` 在未来的问题。每个测试方法都会重置数据库，所以第一个问题不再存在，因此索引中也不应该有任何问题。

以此类推。实际上，我们正在使用这些测试来讲述一个关于管理员输入和网站用户体验的故事，并检查在系统的每个状态以及状态的每个新变化下，预期结果是否会显示出来。

## 测试 `DetailView`

我们目前所做的工作运行良好；然而，即使未来的问题不在 _索引_ 中显示，但如果用户知道或猜到正确的 URL，他们仍然可以访问它们。所以我们需要在 `DetailView` 中添加类似的约束：

```python
class DetailView(generic.DetailView):
  ...

    def get_queryset(self):
        """
        排除任何尚未发布的问题。
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

然后我们应该添加一些测试，以检查 `pub_date` 在过去的 `Question` 是否可以显示，而 `pub_date` 在未来的是否不可以显示：

```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        未来发布时间的问题的详细视图返回404未找到。
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        过去发布时间的问题的详细视图显示问题的文本。
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

## 更多测试的想法

我们应该为 `ResultsView` 添加一个类似的 `get_queryset` 方法，并为该视图创建一个新的测试类。这将与我们刚刚创建的非常相似；实际上会有很多重复。

我们还可以通过其他方式改进我们的应用程序，并在这个过程中添加测试。例如，没有 `Choices` 的 `Question` 可以在网站上发布是很愚蠢的。所以，我们的视图可以检查这一点，并排除这样的 `Question`。我们的测试将创建一个没有 `Choices` 的 `Question`，然后测试它不会被发布，同时创建一个有 `Choices` 的类似 `Question`，并测试它会被发布。

也许登录的管理员用户应该被允许查看未发布的 `Question`，但普通访客不可以。同样：无论为实现此目的需要在软件中添加什么，都应该伴随着一个测试，无论你是先编写测试然后使代码通过测试，还是先在代码中制定逻辑然后编写测试来证明它。

在某个时候，你肯定会看看你的测试，并想知道你的代码是否存在测试臃肿的问题，这就引出了：
