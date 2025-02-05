# 自定义管理界面的外观和感觉

显然，在每个管理页面顶部显示“Django 管理”是很荒谬的。这只是占位文本。

不过，你可以使用 Django 的模板系统来更改它。Django 管理界面由 Django 自身提供支持，其界面使用 Django 自己的模板系统。

## 自定义项目模板

在你的项目目录（即包含 `manage.py` 的目录）中创建一个 `templates` 目录。模板可以存放在 Django 能够访问的文件系统的任何位置。（Django 以服务器运行的用户身份运行。）然而，将模板保存在项目内部是一个值得遵循的良好惯例。

打开你的设置文件（记得是 `mysite/settings.py`），并在 `TEMPLATES` 设置中添加一个 `DIRS <TEMPLATES-DIRS>` 选项：

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

`DIRS <TEMPLATES-DIRS>` 是一个文件系统目录列表，在加载 Django 模板时会检查这些目录；它是一个搜索路径。

## 组织模板

就像静态文件一样，我们本可以把所有模板都放在一个大的 `templates` 目录中，这样也能完美运行。然而，属于特定应用的模板应该放在该应用的模板目录（例如 `polls/templates`）中，而不是项目的（`templates`）。我们将在《可复用应用教程》（/intro/reusable-apps）中更详细地讨论这样做的原因。

现在在 `templates` 目录内创建一个名为 `admin` 的目录，并将 Django 自身源代码中默认的 Django 管理模板目录（`django/contrib/admin/templates`）中的模板 `admin/base_site.html` 复制到该目录中。

## Django 源文件在哪里？

如果你在系统上难以找到 Django 源文件的位置，可以运行以下命令：

```bash
python -c "import django; print(django.__path__)"
```

```plaintext
['/home/labex/.local/lib/python3.10/site-packages/django']
```

然后，编辑该文件，将 `{{ site_header|default:_('Django administration') }}`（包括花括号）替换为你认为合适的你自己网站的名称。你最终应该得到一段类似这样的代码：

```html+django
{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a><div>
{% endblock %}
```

我们使用这种方法来教你如何覆盖模板。在实际项目中，你可能会使用 `django.contrib.admin.AdminSite.site_header` 属性来更轻松地进行这种特定的定制。

这个模板文件包含很多像 `{% block branding %}` 和 `{{ title }}` 这样的文本。`{%` 和 `{{` 标签是 Django 模板语言的一部分。当 Django 渲染 `admin/base_site.html` 时，这种模板语言将被求值以生成最终的 HTML 页面，就像我们在《创建公共接口视图》中看到的那样。

请注意，Django 的任何默认管理模板都可以被覆盖。要覆盖一个模板，按照你对 `base_site.html` 所做的操作进行 —— 从默认目录复制到你的自定义目录，并进行更改。

## 自定义应用的模板

敏锐的读者可能会问：但是如果 `DIRS <TEMPLATES-DIRS>` 默认是空的，Django 是如何找到默认的管理模板的呢？答案是，由于 `APP_DIRS <TEMPLATES-APP_DIRS>` 被设置为 `True`，Django 会自动在每个应用包内查找一个 `templates/` 子目录，用作备用（别忘了 `django.contrib.admin` 是一个应用）。

我们的投票应用不是很复杂，不需要自定义管理模板。但是如果它变得更复杂，并且需要为其某些功能修改 Django 的标准管理模板，那么修改应用的模板而不是项目的模板会更明智。这样，你可以将投票应用包含在任何新项目中，并确保它能找到所需的自定义模板。

有关 Django 如何查找其模板的更多信息，请参阅《模板加载文档》（template-loading）。
