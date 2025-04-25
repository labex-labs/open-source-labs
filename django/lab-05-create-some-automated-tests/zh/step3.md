# 编写我们的第一个测试

## 我们发现一个漏洞

幸运的是，“投票”应用程序中有一个小漏洞需要我们立即修复：`Question.was_published_recently()` 方法在 `Question` 的发布时间在过去一天内时返回 `True`（这是正确的），但当 `Question` 的 `pub_date` 字段在未来时也返回 `True`（这显然不对）。

通过使用 `shell` 检查一个发布时间在未来的问题的该方法来确认这个漏洞：

```bash
cd ~/project/mysite
python manage.py shell
```

```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # 创建一个发布时间在未来 30 天的 Question 实例
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # 它是最近发布的吗？
>>> future_question.was_published_recently()
True
```

由于未来的事情不是“最近”发生的，这显然是错误的。

## 创建一个测试来暴露这个漏洞

我们刚才在 `shell` 中为测试这个问题所做的操作，正是我们在自动化测试中可以做的，所以让我们把它变成一个自动化测试。

应用程序测试的常规位置是在应用程序的 `tests.py` 文件中；测试系统会自动在任何以 `test` 开头的文件中找到测试。

在“投票”应用程序的 `tests.py` 文件中放入以下内容：

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        对于发布时间在未来的问题，was_published_recently() 返回 False。
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

在这里，我们创建了一个 `django.test.TestCase` 的子类，其中有一个方法创建了一个发布时间在未来的 `Question` 实例。然后我们检查 `was_published_recently()` 的输出——它应该是 `False`。

## 运行测试

在终端中，我们可以运行我们的测试：

```bash
python manage.py test polls
```

你会看到类似这样的内容：

```shell
[object Object]
```

> 不同的错误？

如果你在这里得到一个 `NameError`，你可能在《教程 02 - 导入时区》的第 2 部分中遗漏了一个步骤，我们在那里将 `datetime` 和 `timezone` 的导入添加到了 `polls/models.py` 中。从该部分复制导入内容，然后再次尝试运行你的测试。

发生的情况如下：

- `manage.py test polls` 在“投票”应用程序中查找测试
- 它找到了 `django.test.TestCase` 类的一个子类
- 它为测试目的创建了一个特殊的数据库
- 它查找测试方法——那些名字以 `test` 开头的方法
- 在 `test_was_published_recently_with_future_question` 中，它创建了一个 `Question` 实例，其 `pub_date` 字段在未来 30 天
- …… 并使用 `assertIs()` 方法，它发现其 `was_published_recently()` 返回 `True`，尽管我们希望它返回 `False`

测试告诉我们哪个测试失败了，甚至是失败发生的行。

## 修复漏洞

我们已经知道问题所在：如果 `Question` 的 `pub_date` 在未来，`Question.was_published_recently()` 应该返回 `False`。在 `models.py` 中修改该方法，使其仅在日期也在过去时才返回 `True`：

```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

然后再次运行测试：

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

在发现一个漏洞后，我们编写了一个测试来暴露它，并在代码中纠正了这个漏洞，这样我们的测试就通过了。

未来我们的应用程序可能还会出现许多其他问题，但我们可以确定不会无意中重新引入这个漏洞，因为运行测试会立即警告我们。我们可以认为应用程序的这一小部分永远安全地确定下来了。

## 更全面的测试

既然我们在这里，我们可以进一步确定 `was_published_recently()` 方法；实际上，如果在修复一个漏洞时又引入了另一个漏洞，那将是非常尴尬的。

在同一个类中再添加两个测试方法，以更全面地测试该方法的行为：

```python
def test_was_published_recently_with_old_question(self):
    """
    对于发布时间早于 1 天的问题，was_published_recently() 返回 False。
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    对于发布时间在过去一天内的问题，was_published_recently() 返回 True。
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

现在我们有三个测试来确认 `Question.was_published_recently()` 对于过去、最近和未来的问题都返回合理的值。

同样，“投票”是一个最小化的应用程序，但无论它未来变得多么复杂，以及它与其他代码如何交互，我们现在有了一些保证，即我们为其编写测试的方法将按预期方式运行。
