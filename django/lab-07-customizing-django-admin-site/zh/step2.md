# 添加关联对象

好的，我们已经有了问题管理页面，但是一个 `Question` 有多个 `Choice`，而管理页面并没有显示选项。

不过，马上就会显示了。

有两种方法可以解决这个问题。第一种方法是像注册 `Question` 一样向管理站点注册 `Choice`：

```python
from django.contrib import admin

from.models import Choice, Question

#...
admin.site.register(Choice)
```

现在，“选项”在 Django 管理站点中是一个可用选项。“添加选项”表单如下所示：

![添加选项表单界面](../assets/20230908-16-09-57-eCXIdjZu.png)

在那个表单中，“问题”字段是一个下拉框，包含数据库中的每个问题。Django 知道 `~django.db.models.ForeignKey` 在管理站点中应该表示为一个 `<select>` 框。在我们的例子中，此时只有一个问题。

还要注意“问题”旁边的“添加另一个问题”链接。与另一个对象具有 `ForeignKey` 关系的每个对象都会自动获得这个链接。当你点击“添加另一个问题”时，会弹出一个带有“添加问题”表单的窗口。如果你在那个窗口中添加一个问题并点击“保存”，Django 会将问题保存到数据库中，并在你正在查看的“添加选项”表单上动态地将其添加为所选选项。

但是，实际上，这是一种向系统中添加 `Choice` 对象的低效方式。如果能在创建 `Question` 对象时直接添加一堆选项，那就更好了。让我们来实现这一点。

删除对 `Choice` 模型的 `register()` 调用。然后，编辑 `Question` 的注册代码如下：

```python
from django.contrib import admin

from.models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("日期信息", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```

这告诉 Django：“`Choice` 对象在 `Question` 管理页面上进行编辑。默认情况下，提供足够的字段用于 3 个选项。”

加载“添加问题”页面，看看效果如何：

![带有选项的问题管理页面](../assets/20230908-16-11-09-tVqaXrGB.png)

它的工作原理如下：有三个用于关联选项的插槽 —— 由 `extra` 指定 —— 并且每次你回到已创建对象的“更改”页面时，都会再得到另外三个额外的插槽。

在当前三个插槽的末尾，你会找到一个“添加另一个选项”链接。如果你点击它，会添加一个新的插槽。如果你想删除添加的插槽，可以点击添加插槽右上角的 X。这张图片展示了一个添加的插槽：

![动态添加的额外插槽](../assets/admin14t.png)

不过，有一个小问题。显示用于输入关联 `Choice` 对象的所有字段会占用大量屏幕空间。因此，Django 提供了一种以表格形式显示内联关联对象的方式。要使用它，将 `ChoiceInline` 声明改为：

```python
class ChoiceInline(admin.TabularInline):
  ...
```

使用 `TabularInline`（而不是 `StackedInline`），关联对象将以更紧凑的基于表格的格式显示：

![表格形式的内联选项显示](../assets/20230908-16-12-24-1nqRkbAI.png)

请注意，有一个额外的“删除？”列，允许删除使用“添加另一个选项”按钮添加的行以及已经保存的行。
