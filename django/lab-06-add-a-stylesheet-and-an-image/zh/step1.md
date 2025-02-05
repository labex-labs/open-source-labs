# 自定义应用的外观

首先，在你的 `polls` 目录中创建一个名为 `static` 的目录。Django 会在那里查找静态文件，这与 Django 在 `polls/templates/` 中查找模板的方式类似。

Django 的 `STATICFILES_FINDERS` 设置包含一个查找器列表，这些查找器知道如何从各种来源发现静态文件。其中一个默认查找器是 `AppDirectoriesFinder`，它会在每个 `INSTALLED_APPS` 中查找一个 “static” 子目录，就像我们刚刚在 `polls` 中创建的那个一样。管理站点对其静态文件使用相同的目录结构。

在你刚刚创建的 `static` 目录中，再创建一个名为 `polls` 的目录，并在其中创建一个名为 `style.css` 的文件。换句话说，你的样式表应该位于 `polls/static/polls/style.css`。由于 `AppDirectoriesFinder` 静态文件查找器的工作方式，你可以在 Django 中将此静态文件引用为 `polls/style.css`，类似于你引用模板路径的方式。

## 静态文件命名空间

就像模板一样，我们 _也许_ 可以直接将静态文件放在 `polls/static` 中（而不是再创建一个 `polls` 子目录），但这实际上是个坏主意。Django 会选择它找到的第一个名称匹配的静态文件，如果你在 _另一个_ 应用中有一个同名的静态文件，Django 将无法区分它们。我们需要能够让 Django 指向正确的文件，而确保这一点的最佳方法是通过 _命名空间_ 它们。也就是说，将这些静态文件放在另一个以应用本身命名的目录中。

将以下代码放入该样式表（`polls/static/polls/style.css`）：

```css
li a {
  color: green;
}
```

接下来，在 `polls/templates/polls/index.html` 的顶部添加以下内容：

```html+django
{% load static %}

<link rel="stylesheet" href="{% static 'polls/style.css' %}">
```

`{% static %}` 模板标签会生成静态文件的绝对 URL。

这就是开发时你需要做的全部。

启动服务器（如果它已经在运行则重启）：

```bash
python manage.py runserver 0.0.0.0:8080
```

重新加载 **Web 8080** 标签页，你应该会看到问题链接是绿色的（Django 风格！），这意味着你的样式表已正确加载。

![绿色问题链接示例](../assets/20230908-15-29-11-ztyI1umP.png)
