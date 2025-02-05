# 创建模型

现在我们将定义你的模型 —— 本质上就是你的数据库布局，并附带额外的元数据。

模型是关于你的数据的唯一权威信息源。它包含了你正在存储的数据的基本字段和行为。Django遵循 `DRY原则 <dry>`。目标是在一个地方定义你的数据模型，并从中自动派生其他内容。

这包括迁移 —— 例如，与Ruby On Rails不同，迁移完全从你的模型文件派生而来，本质上是Django可以遍历的历史记录，用于更新你的数据库模式以匹配当前模型。

在我们的投票应用中，我们将创建两个模型：`Question`（问题）和 `Choice`（选项）。一个 `Question` 有一个问题和一个发布日期。一个 `Choice` 有两个字段：选项的文本和投票计数。每个 `Choice` 都与一个 `Question` 相关联。

这些概念由Python类表示。编辑 `polls/models.py` 文件，使其如下所示：

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

在这里，每个模型由一个继承自 `django.db.models.Model` 的类表示。每个模型都有许多类变量，每个类变量都表示模型中的一个数据库字段。

每个字段由一个 `~django.db.models.Field` 类的实例表示 —— 例如，字符字段用 `~django.db.models.CharField` 表示，日期时间字段用 `~django.db.models.DateTimeField` 表示。这告诉Django每个字段存储的数据类型。

每个 `~django.db.models.Field` 实例的名称（例如 `question_text` 或 `pub_date`）是字段的名称，采用机器友好的格式。你将在Python代码中使用这个值，并且你的数据库将使用它作为列名。

你可以使用 `~django.db.models.Field` 的第一个可选位置参数来指定一个人类可读的名称。这在Django的一些自省部分中使用，并且它还可以作为文档。如果没有提供这个字段，Django将使用机器可读的名称。在这个例子中，我们只为 `Question.pub_date` 定义了一个人类可读的名称。对于这个模型中的所有其他字段，字段的机器可读名称就足以作为它的人类可读名称。

一些 `~django.db.models.Field` 类有必需的参数。例如，`~django.db.models.CharField` 要求你给它一个 `~django.db.models.CharField.max_length`。这不仅用于数据库模式，还用于验证，我们很快就会看到。

一个 `~django.db.models.Field` 也可以有各种可选参数；在这种情况下，我们将 `votes` 的 `~django.db.models.Field.default` 值设置为0。

最后，请注意使用 `~django.db.models.ForeignKey` 定义了一种关系。这告诉Django每个 `Choice` 都与一个 `Question` 相关。Django支持所有常见的数据库关系：多对一、多对多和一对一。
