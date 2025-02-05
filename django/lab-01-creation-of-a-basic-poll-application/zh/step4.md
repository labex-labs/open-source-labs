# 创建 Polls 应用

既然你的环境（一个「项目」）已经设置好了，你就可以开始工作了。

你在 Django 中编写的每个应用都由一个遵循特定约定的 Python 包组成。Django 提供了一个实用工具，可以自动生成应用的基本目录结构，这样你就可以专注于编写代码，而不必创建目录。

> 项目与应用
> 项目和应用有什么区别？应用是一个能做某些事情的 Web 应用程序——例如，一个博客系统、一个公共记录数据库或一个小型投票应用。项目是特定网站的配置和应用的集合。一个项目可以包含多个应用。一个应用可以存在于多个项目中。

你的应用可以位于 `Python 路径 <tut-searchpath>` 上的任何位置。在本教程中，我们将在与 `manage.py` 文件相同的目录中创建我们的投票应用，以便它可以作为自己的顶级模块导入，而不是作为 `mysite` 的子模块。

要创建你的应用，确保你在与 `manage.py` 相同的目录中，然后输入以下命令：

```bash
cd ~/project/mysite
python manage.py startapp polls
```

这将创建一个名为 `polls` 的目录，其结构如下：

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

这个目录结构将容纳投票应用。
