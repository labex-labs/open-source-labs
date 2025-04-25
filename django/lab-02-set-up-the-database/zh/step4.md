# 玩转 API

现在，让我们进入交互式 Python shell，来体验一下 Django 为你提供的免费 API。要调用 Python shell，使用以下命令：

```bash
python manage.py shell
```

我们使用这个命令而不是简单地输入“python”，是因为 `manage.py` 设置了 `DJANGO_SETTINGS_MODULE` 环境变量，它为 Django 提供了到你的 `mysite/settings.py` 文件的 Python 导入路径。

进入 shell 后，探索一下 `数据库API </topics/db/queries>`：

```python
>>> from polls.models import Choice, Question  # 导入我们刚刚编写的模型类。

# 系统中还没有问题。
>>> Question.objects.all()
<QuerySet []>

# 创建一个新问题。
# 默认设置文件中启用了时区支持，所以
# Django 期望 pub_date 是一个带有时区信息的 datetime。使用 timezone.now()
# 而不是 datetime.datetime.now()，它会处理正确的事情。
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# 将对象保存到数据库中。你必须显式调用 save()。
>>> q.save()

# 现在它有一个 ID 了。
>>> q.id
1

# 通过 Python 属性访问模型字段值。
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2023, 9, 7, 1, 18, 48, 335644, tzinfo=datetime.timezone.utc)

# 通过更改属性然后调用 save() 来更改值。
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() 显示数据库中的所有问题。
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

等一下。`<Question: Question object (1)>` 对这个对象的表示没什么用。让我们通过编辑 `Question` 模型（在 `polls/models.py` 文件中）并为 `Question` 和 `Choice` 添加一个 `~django.db.models.Model.__str__` 方法来解决这个问题：

```python
from django.db import models


class Question(models.Model):
    #...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    #...
    def __str__(self):
        return self.choice_text
```

为你的模型添加 `~django.db.models.Model.__str__` 方法很重要，这不仅对你在处理交互式提示符时方便，而且因为对象的表示在 Django 自动生成的管理界面中到处都有用到。

让我们也为这个模型添加一个自定义方法：

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    #...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

注意添加了 `import datetime` 和 `from django.utils import timezone`，分别用于引用 Python 的标准 `datetime` 模块和 Django 在 `django.utils.timezone` 中与时区相关的实用工具。如果你不熟悉 Python 中的时区处理，可以在 `时区支持文档 </topics/i18n/timezones>` 中了解更多。

保存这些更改，然后通过 **再次运行 `python manage.py shell`** 启动一个新的 Python 交互式 shell：

```python
>>> from polls.models import Choice, Question

# 确保我们添加的 __str__() 方法起作用了。
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django 提供了一个丰富的数据库查找 API，它完全由
# 关键字参数驱动。
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# 获取今年发布的问题。
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# 请求一个不存在的 ID，这将引发一个异常。
>>> Question.objects.get(id=2)
Traceback (most recent call last):
 ...
DoesNotExist: Question matching query does not exist.

# 通过主键查找是最常见的情况，所以 Django 提供了一个
# 主键精确查找的快捷方式。
# 以下与 Question.objects.get(id=1) 相同。
>>> Question.objects.get(pk=1)
<Question: What's up?>

# 确保我们的自定义方法起作用了。
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# 给这个问题添加几个选项。create 调用构造一个新的
# Choice 对象，执行 INSERT 语句，将选项添加到可用选项集中
# 并返回新的 Choice 对象。Django 创建一个集合来保存
# 外键关系的“另一边”
# （例如，一个问题的选项），可以通过 API 访问。
>>> q = Question.objects.get(pk=1)

# 显示相关对象集中的任何选项 —— 目前还没有。
>>> q.choice_set.all()
<QuerySet []>

# 创建三个选项。
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice 对象可以通过 API 访问其相关的 Question 对象。
>>> c.question
<Question: What's up?>

# 反之亦然：Question 对象可以访问 Choice 对象。
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# API 会根据你的需要自动跟踪关系。
# 使用双下划线分隔关系。
# 这可以深入任意多层；没有限制。
# 找到今年发布的任何问题的所有选项
# （重用我们上面创建的 'current_year' 变量）。
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# 让我们删除其中一个选项。使用 delete() 来删除。
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

有关模型关系的更多信息，请参阅 `访问相关对象
</ref/models/relations>`。有关如何使用双下划线通过API执行字段查找的更多信息，请参阅 `字段查找 <field-lookups-intro>`。有关数据库API的完整详细信息，请参阅我们的 `数据库 API 参考
</topics/db/queries>`。
