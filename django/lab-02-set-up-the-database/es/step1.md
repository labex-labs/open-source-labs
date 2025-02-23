# Configuración de la base de datos

Ahora, abra `mysite/settings.py`. Es un módulo de Python normal con variables de nivel de módulo que representan las configuraciones de Django.

Por defecto, la configuración utiliza SQLite. Si es nuevo en bases de datos o solo está interesado en probar Django, esta es la opción más fácil. SQLite está incluido en Python, por lo que no necesitará instalar nada más para admitir su base de datos. Sin embargo, al comenzar su primer proyecto real, es posible que desee usar una base de datos más escalable, como PostgreSQL, para evitar problemas al cambiar de base de datos más adelante.

Si desea usar otra base de datos, instale los `enlaces de base de datos <database-installation>` adecuados y cambie las siguientes claves en el elemento `'default'` de `DATABASES` para que coincidan con sus configuraciones de conexión a la base de datos:

- `ENGINE <DATABASE-ENGINE>` -- Puede ser `'django.db.backends.sqlite3'`, `'django.db.backends.postgresql'`, `'django.db.backends.mysql'` o `'django.db.backends.oracle'`. También están disponibles otros backends <third-party-notes>.
- `NAME` -- El nombre de su base de datos. Si está usando SQLite, la base de datos será un archivo en su computadora; en ese caso, `NAME` debe ser la ruta absoluta completa, incluyendo el nombre de archivo, de ese archivo. El valor predeterminado, `BASE_DIR / 'db.sqlite3'`, almacenará el archivo en el directorio de su proyecto.

Si no está usando SQLite como su base de datos, deben agregarse ajustes adicionales, como `USER`, `PASSWORD` y `HOST`. Para obtener más detalles, consulte la documentación de referencia de `DATABASES`.

> Para bases de datos diferentes a SQLite

Si está usando una base de datos diferente a SQLite, asegúrese de haber creado una base de datos en este momento. Haga eso con "`CREATE DATABASE database_name;`" dentro del prompt interactivo de su base de datos.

También asegúrese de que el usuario de la base de datos proporcionado en `mysite/settings.py` tenga privilegios de "crear base de datos". Esto permite la creación automática de una `base de datos de prueba <the-test-database>` que se necesitará en un tutorial posterior.

Si está usando SQLite, no necesita crear nada previamente: el archivo de base de datos se creará automáticamente cuando sea necesario.

Mientras edita `mysite/settings.py`, establezca `TIME_ZONE` en su zona horaria.

También, observe la configuración `INSTALLED_APPS` en la parte superior del archivo. Esa contiene los nombres de todas las aplicaciones de Django que se activan en esta instancia de Django. Las aplicaciones se pueden usar en múltiples proyectos y se pueden empaquetar y distribuir para que otros las usen en sus proyectos.

Por defecto, `INSTALLED_APPS` contiene las siguientes aplicaciones, todas las cuales vienen con Django:

- `django.contrib.admin` -- El sitio de administración. Lo usará pronto.
- `django.contrib.auth` -- Un sistema de autenticación.
- `django.contrib.contenttypes` -- Un marco para tipos de contenido.
- `django.contrib.sessions` -- Un marco de sesiones.
- `django.contrib.messages` -- Un marco de mensajes.
- `django.contrib.staticfiles` -- Un marco para administrar archivos estáticos.

Estas aplicaciones se incluyen por defecto como una conveniencia para el caso común.

Sin embargo, algunas de estas aplicaciones utilizan al menos una tabla de base de datos, por lo que necesitamos crear las tablas en la base de datos antes de poder utilizarlas. Para hacer eso, ejecute el siguiente comando:

```bash
cd ~/project/mysite
python manage.py migrate
```

```plaintext
Operaciones a realizar:
  Aplicar todas las migraciones: admin, auth, contenttypes, sessions
Ejecutando migraciones:
  Aplicando contenttypes.0001_initial... OK
  Aplicando auth.0001_initial... OK
  Aplicando admin.0001_initial... OK
  Aplicando admin.0002_logentry_remove_auto_add... OK
  Aplicando admin.0003_logentry_add_action_flag_choices... OK
  Aplicando contenttypes.0002_remove_content_type_name... OK
  Aplicando auth.0002_alter_permission_name_max_length... OK
  Aplicando auth.0003_alter_user_email_max_length... OK
  Aplicando auth.0004_alter_user_username_opts... OK
  Aplicando auth.0005_alter_user_last_login_null... OK
  Aplicando auth.0006_require_contenttypes_0002... OK
  Aplicando auth.0007_alter_validators_add_error_messages... OK
  Aplicando auth.0008_alter_user_username_max_length... OK
  Aplicando auth.0009_alter_user_last_name_max_length... OK
  Aplicando auth.0010_alter_group_name_max_length... OK
  Aplicando auth.0011_update_proxy_permissions... OK
  Aplicando auth.0012_alter_user_first_name_max_length... OK
  Aplicando sessions.0001_initial... OK
```

El comando `migrate` examina la configuración `INSTALLED_APPS` y crea cualquier tabla de base de datos necesaria de acuerdo con las configuraciones de la base de datos en su archivo `mysite/settings.py` y las migraciones de la base de datos enviadas con la aplicación (veremos eso más adelante). Verá un mensaje para cada migración que aplica. Si está interesado, ejecute el cliente de línea de comandos de su base de datos y escriba `\dt` (PostgreSQL), `SHOW TABLES;` (MariaDB, MySQL), `.tables` (SQLite) o `SELECT TABLE_NAME FROM USER_TABLES;` (Oracle) para mostrar las tablas que Django creó.

> Para los minimalistas

Como dijimos anteriormente, las aplicaciones predeterminadas se incluyen para el caso común, pero no todos necesitan todas ellas. Si no necesita ninguna o todas ellas, puede comentar o eliminar la línea adecuada de `INSTALLED_APPS` antes de ejecutar `migrate`. El comando `migrate` solo ejecutará migraciones para las aplicaciones en `INSTALLED_APPS`.
