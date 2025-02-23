# Erstellen der Umfrage-App

Jetzt, da Ihre Umgebung – ein „Projekt“ – eingerichtet ist, sind Sie bereit, an der Arbeit zu beginnen.

Jede Anwendung, die Sie in Django schreiben, besteht aus einem Python-Paket, das einer bestimmten Konvention folgt. Django bietet ein Tool, das automatisch die grundlegende Verzeichnisstruktur einer App erstellt, sodass Sie sich auf den Code schreiben können, anstatt Verzeichnisse zu erstellen.

> Projekte vs. Apps
> Was ist der Unterschied zwischen einem Projekt und einer App? Eine App ist eine Webanwendung, die etwas macht – z.B. ein Blogsystem, eine Datenbank öffentlicher Akten oder eine kleine Umfrage-App. Ein Projekt ist eine Sammlung von Konfigurationen und Apps für eine bestimmte Website. Ein Projekt kann mehrere Apps enthalten. Eine App kann in mehreren Projekten vorhanden sein.

Ihre Apps können sich an beliebiger Stelle auf Ihrem `Python-Pfad <tut-searchpath>` befinden. In diesem Tutorial erstellen wir unsere Umfrage-App im selben Verzeichnis wie Ihre `manage.py`-Datei, sodass sie als eigenes Top-Level-Modul importiert werden kann, anstatt als Untermodul von `mysite`.

Um Ihre App zu erstellen, stellen Sie sicher, dass Sie sich im selben Verzeichnis wie `manage.py` befinden, und geben Sie diesen Befehl ein:

```bash
cd ~/project/mysite
python manage.py startapp polls
```

Das erstellt ein Verzeichnis `polls`, das wie folgt aufgebaut ist:

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

Diese Verzeichnisstruktur wird die Umfrageanwendung beherbergen.
