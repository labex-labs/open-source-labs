# 自定义管理更改列表

既然问题管理页面看起来不错了，那我们来对“更改列表”页面做一些调整 —— 就是那个显示系统中所有问题的页面。

目前它是这样的：

![投票应用更改列表页面](../assets/admin04t.png)

默认情况下，Django 显示每个对象的 `str()` 表示。但有时如果我们能显示单个字段会更有帮助。要做到这一点，可以使用 `~django.contrib.admin.ModelAdmin.list_display` 管理选项，它是一个字段名元组，用于在对象的更改列表页面上作为列显示：

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date"]
```

为了保险起见，我们还把《设置数据库》中的 `was_published_recently()` 方法也加上：

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date", "was_published_recently"]
```

现在问题更改列表页面是这样的：

![问题更改列表视图](../assets/20230908-16-14-08-GNY2lggF.png)

你可以点击列标题按这些值进行排序 —— 除了 `was_published_recently` 标题，因为不支持按任意方法的输出进行排序。还要注意，`was_published_recently` 的列标题默认是方法名（下划线替换为空格），并且每行都包含输出的字符串表示。

你可以通过在该方法上使用 `~django.contrib.admin.display` 装饰器（在 `polls/models.py` 中）来改进这一点，如下所示：

```python
from django.contrib import admin


class Question(models.Model):
    #...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="最近发布？",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

有关可通过装饰器配置的属性的更多信息，请参阅 `~django.contrib.admin.ModelAdmin.list_display`。

再次编辑你的 `polls/admin.py` 文件，并对 `Question` 更改列表页面进行改进：使用 `~django.contrib.admin.ModelAdmin.list_filter` 进行过滤。在 `QuestionAdmin` 中添加以下行：

```python
list_filter = ["pub_date"]
```

这会添加一个“过滤”侧边栏，让人们可以按 `pub_date` 字段过滤更改列表：

![管理列表过滤侧边栏](../assets/20230908-16-16-39-otfMNyYo.png)

显示的过滤器类型取决于你正在过滤的字段类型。因为 `pub_date` 是一个 `~django.db.models.DateTimeField`，Django 知道要给出适当的过滤选项：“任何日期”、“今天”、“过去7天”、“本月”、“今年”。

这看起来很不错了。让我们添加一些搜索功能：

```python
search_fields = ["question_text"]
```

这会在更改列表顶部添加一个搜索框。当有人输入搜索词时，Django 将在 `question_text` 字段中进行搜索。你可以使用任意多个字段 —— 不过因为它在幕后使用 `LIKE` 查询，将搜索字段数量限制在合理数量会让你的数据库更容易进行搜索。

现在也是时候注意一下更改列表会自动提供分页功能了。默认是每页显示100项。`更改列表分页 <django.contrib.admin.ModelAdmin.list_per_page>`、`搜索框 <django.contrib.admin.ModelAdmin.search_fields>`、`过滤器 <django.contrib.admin.ModelAdmin.list_filter>`、`日期层次结构 <django.contrib.admin.ModelAdmin.date_hierarchy>` 和 `列标题排序 <django.contrib.admin.ModelAdmin.list_display>` 都能像你期望的那样协同工作。
