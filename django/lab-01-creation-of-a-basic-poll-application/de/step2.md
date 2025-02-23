# Ein Projekt erstellen

Wenn Sie Django zum ersten Mal verwenden, müssen Sie einige initiale Einstellungen vornehmen. Namentlich müssen Sie automatisch Code generieren, der ein Django-`Projekt` erstellt – eine Sammlung von Einstellungen für eine Django-Instanz, einschließlich der Datenbankkonfiguration, Django-spezifischer Optionen und anwendungsspezifischer Einstellungen.

Öffnen Sie eine Befehlszeile, navigieren Sie mit `cd` in ein Verzeichnis, in dem Sie Ihren Code speichern möchten, und führen Sie dann folgenden Befehl aus:

```bash
cd ~/project
django-admin startproject mysite
```

Dies erstellt ein Verzeichnis `mysite` im aktuellen Verzeichnis.

Schauen wir uns an, was `startproject` erstellt hat:

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

Diese Dateien sind:

- Das äußere `mysite/`-Wurzelverzeichnis ist ein Container für Ihr Projekt. Sein Name spielt für Django keine Rolle; Sie können es in irgendeinen Namen umbenennen, den Sie möchten.
- `manage.py`: Ein Befehlszeilenwerkzeug, das Ihnen ermöglicht, mit diesem Django-Projekt auf verschiedene Weise zu interagieren.
- Das innere `mysite/`-Verzeichnis ist das tatsächliche Python-Paket für Ihr Projekt. Sein Name ist der Python-Paketname, den Sie verwenden müssen, um etwas darin zu importieren (z.B. `mysite.urls`).
- `mysite/__init__.py`: Eine leere Datei, die Python mitteilt, dass dieses Verzeichnis als Python-Paket betrachtet werden soll.
- `mysite/settings.py`: Einstellungen/Konfiguration für dieses Django-Projekt.
- `mysite/urls.py`: Die URL-Deklarationen für dieses Django-Projekt; ein „Inhaltsverzeichnis“ Ihrer von Django betriebenen Website.
- `mysite/asgi.py`: Ein Einstiegspunkt für ASGI-kompatible Webdienste, um Ihr Projekt bereitzustellen.
- `mysite/wsgi.py`: Ein Einstiegspunkt für WSGI-kompatible Webdienste, um Ihr Projekt bereitzustellen.
