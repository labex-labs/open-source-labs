# Настройка базы данных

Теперь откройте `mysite/settings.py`. Это обычный Python-модуль с переменными уровня модуля, представляющими настройки Django.

По умолчанию конфигурация использует SQLite. Если вы впервые сталкиваетесь с базами данных или просто хотите попробовать Django, это самый простой выбор. SQLite входит в состав Python, поэтому вам не нужно ничего дополнительно устанавливать для поддержки своей базы данных. Однако, когда вы начинаете свой первый настоящий проект, вы, возможно, захотите использовать более масштабируемую базу данных, например, PostgreSQL, чтобы избежать головной боли при смене базы данных впоследствии.

Если вы хотите использовать другую базу данных, установите соответствующие `биндинги базы данных <database-installation>` и измените следующие ключи в элементе `'default'` словаря `DATABASES`, чтобы они соответствовали вашим настройкам подключения к базе данных:

- `ENGINE <DATABASE-ENGINE>` -- Либо `'django.db.backends.sqlite3'`, `'django.db.backends.postgresql'`, `'django.db.backends.mysql'` или `'django.db.backends.oracle'`. Доступны и другие бэкенды <third-party-notes>.
- `NAME` -- Имя вашей базы данных. Если вы используете SQLite, база данных будет файлом на вашем компьютере; в этом случае `NAME` должен быть полным абсолютным путём, включая имя файла, к этому файлу. Значение по умолчанию, `BASE_DIR / 'db.sqlite3'`, сохранит файл в директории вашего проекта.

Если вы не используете SQLite в качестве своей базы данных, необходимо добавить дополнительные настройки, такие как `USER`, `PASSWORD` и `HOST`. Подробнее см. в справочной документации по `DATABASES`.

> Для баз данных, отличных от SQLite

Если вы используете базу данных, отличную от SQLite, убедитесь, что вы создали базу данных к этому времени. Сделайте это с помощью команды "`CREATE DATABASE database_name;`" в интерактивном提示符 вашей базы данных.

Также убедитесь, что пользователь базы данных, указанный в `mysite/settings.py`, имеет права "создавать базу данных". Это позволяет автоматически создавать `тестовую базу данных <the-test-database>`, которая понадобится в последующем туториале.

Если вы используете SQLite, вы не нужно создавать ничего заранее - файл базы данных будет создан автоматически, когда он понадобится.

Во время редактирования `mysite/settings.py` установите `TIME_ZONE` в вашу временную зону.

Также обратите внимание на настройку `INSTALLED_APPS` в начале файла. В ней хранятся имена всех Django-приложений, активированных в этом экземпляре Django. Приложения могут использоваться в нескольких проектах, и вы можете упаковать и распространить их для использования другими в своих проектах.

По умолчанию `INSTALLED_APPS` содержит следующие приложения, все они входят в состав Django:

- `django.contrib.admin` -- Административный сайт. Вы вскоре будете с ним работать.
- `django.contrib.auth` -- Система аутентификации.
- `django.contrib.contenttypes` -- Фреймворк для типов содержимого.
- `django.contrib.sessions` -- Фреймворк для сессий.
- `django.contrib.messages` -- Фреймворк для сообщений.
- `django.contrib.staticfiles` -- Фреймворк для управления статическими файлами.

Эти приложения включены по умолчанию для удобства при общем случае.

Однако некоторые из этих приложений используют по крайней мере одну таблицу базы данных, поэтому мы должны создать таблицы в базе данных, прежде чем сможем их использовать. Для этого выполните следующую команду:

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

Команда `migrate` смотрит на настройку `INSTALLED_APPS` и создает любые необходимые таблицы базы данных в соответствии с настройками базы данных в вашем файле `mysite/settings.py` и миграциями базы данных, поставляемыми вместе с приложением (мы поговорим об этом позже). Вы увидите сообщение для каждой миграции, которую она применяет. Если вы заинтересованы, запустите командную оболочку для своей базы данных и введите `\dt` (PostgreSQL), `SHOW TABLES;` (MariaDB, MySQL), `.tables` (SQLite) или `SELECT TABLE_NAME FROM USER_TABLES;` (Oracle), чтобы отобразить таблицы, созданные Django.

> Для минималистов

Как мы говорили выше, стандартные приложения включены для общего случая, но не всем они нужны. Если вы не нуждаетесь в одном или нескольких из них, не стесняйтесь закомментировать или удалить соответствующую строку из `INSTALLED_APPS` перед запуском `migrate`. Команда `migrate` будет выполнять миграции только для приложений в `INSTALLED_APPS`.
