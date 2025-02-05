# 创建项目

如果这是你第一次使用 Django，你需要进行一些初始设置。具体来说，你需要自动生成一些代码来创建一个 Django「项目」——Django 实例的一组设置，包括数据库配置、Django 特定选项和应用程序特定设置。

在命令行中，使用 `cd` 进入你想要存储代码的目录，然后运行以下命令：

```bash
cd ~/project
django-admin startproject mysite
```

这将在当前目录中创建一个 `mysite` 目录。

让我们看看 `startproject` 创建了什么：

```plaintext
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

这些文件分别是：

- 外部的 `mysite/` 根目录是你项目的容器。它的名称对 Django 来说并不重要；你可以将其重命名为任何你喜欢的名称。
- `manage.py`：一个命令行实用工具，可让你以各种方式与这个 Django 项目进行交互。
- 内部的 `mysite/` 目录是你项目实际的 Python 包。它的名称是你在导入其中任何内容时需要使用的 Python 包名称（例如 `mysite.urls`）。
- `mysite/__init__.py`：一个空文件，告诉 Python 这个目录应被视为一个 Python 包。
- `mysite/settings.py`：此 Django 项目的设置/配置。
- `mysite/urls.py`：此 Django 项目的 URL 声明；你基于 Django 的网站的「目录」。
- `mysite/asgi.py`：ASGI 兼容的 Web 服务器为你的项目提供服务的入口点。
- `mysite/wsgi.py`：WSGI 兼容的 Web 服务器为你的项目提供服务的入口点。
