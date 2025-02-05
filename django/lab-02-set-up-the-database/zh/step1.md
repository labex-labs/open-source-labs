# 数据库设置

现在，打开 `mysite/settings.py`。它是一个普通的Python模块，其中的模块级变量代表Django设置。

默认情况下，配置使用SQLite。如果你是数据库新手，或者只是想尝试一下Django，这是最简单的选择。SQLite包含在Python中，所以你不需要安装任何其他东西来支持你的数据库。然而，当你开始第一个实际项目时，你可能想要使用像PostgreSQL这样更具可扩展性的数据库，以避免日后切换数据库带来的麻烦。

如果你希望使用其他数据库，请安装相应的 `数据库绑定 <database-installation>`，并在 `DATABASES` 的 `'default'` 项中更改以下键，以匹配你的数据库连接设置：

- `ENGINE <DATABASE-ENGINE>` -- 可以是 `'django.db.backends.sqlite3'`、`'django.db.backends.postgresql'`、`'django.db.backends.mysql'` 或 `'django.db.backends.oracle'`。其他后端也 `可用<third-party-notes>`。
- `NAME` -- 你的数据库名称。如果你使用SQLite，数据库将是你计算机上的一个文件；在这种情况下，`NAME` 应该是该文件的完整绝对路径，包括文件名。默认值 `BASE_DIR / 'db.sqlite3'` 将把文件存储在你的项目目录中。

如果你不使用SQLite作为数据库，则必须添加其他设置，如 `USER`、`PASSWORD` 和 `HOST`。有关更多详细信息，请参阅 `DATABASES` 的参考文档。

> 对于非SQLite数据库

如果你使用的是除SQLite之外的数据库，请确保此时已经创建了数据库。在数据库的交互式提示符中使用 “`CREATE DATABASE database_name;`” 来创建。

还要确保 `mysite/settings.py` 中提供的数据库用户具有 “创建数据库” 权限。这允许自动创建一个 `测试数据库 <the-test-database>`，这在后面的教程中会用到。

如果你使用SQLite，则无需事先创建任何东西 —— 数据库文件将在需要时自动创建。

在编辑 `mysite/settings.py` 时，将 `TIME_ZONE` 设置为你的时区。

另外，请注意文件顶部的 `INSTALLED_APPS` 设置。它包含在此Django实例中激活的所有Django应用的名称。应用可以在多个项目中使用，你可以打包并分发它们供其他人在他们的项目中使用。

默认情况下，`INSTALLED_APPS` 包含以下所有随Django一起提供的应用：

- `django.contrib.admin` -- 管理站点。你很快就会用到它。
- `django.contrib.auth` -- 一个认证系统。
- `django.contrib.contenttypes` -- 一个内容类型框架。
- `django.contrib.sessions` -- 一个会话框架。
- `django.contrib.messages` -- 一个消息框架。
- `django.contrib.staticfiles` -- 一个管理静态文件的框架。

默认情况下包含这些应用是为了方便常见情况。

不过，其中一些应用至少使用一个数据库表，所以我们需要在数据库中创建表才能使用它们。为此，请运行以下命令：

```bash
cd ~/project/mysite
python manage.py migrate
```

```plaintext
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

`migrate` 命令会查看 `INSTALLED_APPS` 设置，并根据 `mysite/settings.py` 文件中的数据库设置以及应用附带的数据库迁移（我们稍后会介绍）创建任何必要的数据库表。你会看到它应用的每个迁移的消息。如果你感兴趣，可以运行数据库的命令行客户端并输入 `\dt`（PostgreSQL）、`SHOW TABLES;`（MariaDB、MySQL）、`.tables`（SQLite）或 `SELECT TABLE_NAME FROM USER_TABLES;`（Oracle）来显示Django创建的表。

> 对于极简主义者

如我们上面所说，默认应用是为常见情况而包含的，但不是每个人都需要它们。如果你不需要其中任何一个或全部，可以在运行 `migrate` 之前，随意从 `INSTALLED_APPS` 中注释掉或删除相应的行。`migrate` 命令只会运行 `INSTALLED_APPS` 中应用的迁移。
