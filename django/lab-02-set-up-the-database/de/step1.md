# Datenbankeinrichtung

Öffnen Sie nun `mysite/settings.py`. Dies ist ein normales Python-Modul mit Modul-Ebene-Variablen, die die Django-Einstellungen repräsentieren.

Standardmäßig verwendet die Konfiguration SQLite. Wenn Sie neu in Datenbanken sind oder nur daran interessiert sind, Django auszuprobieren, ist dies die einfachste Wahl. SQLite ist in Python enthalten, so dass Sie nichts weiter installieren müssen, um Ihre Datenbank zu unterstützen. Wenn Sie jedoch Ihr erstes echtes Projekt starten möchten, sollten Sie möglicherweise eine skalierbarere Datenbank wie PostgreSQL verwenden, um spätere Kopfschmerzen bei der Datenbankumstellung zu vermeiden.

Wenn Sie eine andere Datenbank verwenden möchten, installieren Sie die entsprechenden `Datenbankbindung <database-installation>` und ändern Sie die folgenden Schlüssel im `DATABASES` `'default'`-Element, um Ihren Datenbankverbindungs-Einstellungen zu entsprechen:

- `ENGINE <DATABASE-ENGINE>` -- Entweder `'django.db.backends.sqlite3'`, `'django.db.backends.postgresql'`, `'django.db.backends.mysql'` oder `'django.db.backends.oracle'`. Andere Backends sind `auch verfügbar <third-party-notes>`.
- `NAME` -- Der Name Ihrer Datenbank. Wenn Sie SQLite verwenden, wird die Datenbank eine Datei auf Ihrem Computer sein; in diesem Fall sollte `NAME` der vollständige absolute Pfad, einschließlich Dateinamen, dieser Datei sein. Der Standardwert `BASE_DIR / 'db.sqlite3'` speichert die Datei im Projektverzeichnis.

Wenn Sie nicht SQLite als Ihre Datenbank verwenden, müssen zusätzliche Einstellungen wie `USER`, `PASSWORD` und `HOST` hinzugefügt werden. Weitere Details finden Sie in der Referenzdokumentation für `DATABASES`.

> Für Nicht-SQLite-Datenbanken

Wenn Sie eine Datenbank außer SQLite verwenden, stellen Sie sicher, dass Sie zu diesem Zeitpunkt eine Datenbank erstellt haben. Machen Sie dies mit "`CREATE DATABASE database_name;`" innerhalb des interaktiven Prompts Ihrer Datenbank.

Stellen Sie auch sicher, dass der Datenbankbenutzer, der in `mysite/settings.py` angegeben ist, über "create database"-Rechte verfügt. Dies ermöglicht die automatische Erstellung einer `Testdatenbank <the-test-database>`, die in einem späteren Tutorial benötigt wird.

Wenn Sie SQLite verwenden, müssen Sie nichts im Voraus erstellen - die Datenbankdatei wird automatisch erstellt, wenn sie benötigt wird.

Während Sie `mysite/settings.py` bearbeiten, legen Sie `TIME_ZONE` auf Ihre Zeitzone fest.

Beachten Sie auch die `INSTALLED_APPS`-Einstellung am Anfang der Datei. Dies enthält die Namen aller Django-Anwendungen, die in dieser Django-Instanz aktiviert sind. Anwendungen können in mehreren Projekten verwendet werden, und Sie können sie verpacken und verteilen, damit andere sie in ihren Projekten verwenden können.

Standardmäßig enthält `INSTALLED_APPS` die folgenden Anwendungen, alle von denen mit Django mitgeliefert werden:

- `django.contrib.admin` -- Die Admin-Site. Sie werden sie bald verwenden.
- `django.contrib.auth` -- Ein Authentifizierungssystem.
- `django.contrib.contenttypes` -- Ein Framework für Inhaltstypen.
- `django.contrib.sessions` -- Ein Sitzungsframework.
- `django.contrib.messages` -- Ein Nachrichtenframework.
- `django.contrib.staticfiles` -- Ein Framework zur Verwaltung von statischen Dateien.

Diese Anwendungen werden standardmäßig als Bequemlichkeit für den üblichen Fall enthalten.

Einige dieser Anwendungen verwenden jedoch mindestens eine Datenbanktabelle, daher müssen wir die Tabellen in der Datenbank erstellen, bevor wir sie verwenden können. Führen Sie dazu den folgenden Befehl aus:

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

Der `migrate`-Befehl betrachtet die `INSTALLED_APPS`-Einstellung und erstellt alle erforderlichen Datenbanktabellen gemäß den Datenbankeinstellungen in Ihrer `mysite/settings.py`-Datei und den Datenbankmigrationen, die mit der App mitgeliefert werden (wir werden diese später behandeln). Sie erhalten eine Meldung für jede Migration, die er anwendet. Wenn Sie interessiert sind, führen Sie den Befehlszeilenclient für Ihre Datenbank aus und geben Sie `\dt` (PostgreSQL), `SHOW TABLES;` (MariaDB, MySQL), `.tables` (SQLite) oder `SELECT TABLE_NAME FROM USER_TABLES;` (Oracle) ein, um die Tabellen anzuzeigen, die Django erstellt hat.

> Für die Minimalisten

Wie oben erwähnt, werden die Standardanwendungen für den üblichen Fall enthalten, aber nicht jeder braucht sie. Wenn Sie keine oder alle von ihnen benötigen, können Sie die entsprechende Zeile(n) in `INSTALLED_APPS` vor dem Ausführen von `migrate` auskommentieren oder löschen. Der `migrate`-Befehl führt nur Migrationen für Apps in `INSTALLED_APPS` aus.
