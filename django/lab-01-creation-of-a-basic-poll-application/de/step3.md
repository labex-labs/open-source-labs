# Der Entwicklungsserver

Lassen Sie uns überprüfen, ob Ihr Django-Projekt funktioniert. Wechseln Sie in das äußere `mysite`-Verzeichnis, wenn Sie es noch nicht getan haben, und führen Sie die folgenden Befehle aus:

```bash
cd ~/project/mysite
python manage.py runserver
```

Auf der Befehlszeile sehen Sie die folgende Ausgabe:

```plaintext
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.

- 15:50:53 Django version, using settings'mysite.settings' Starting development server at <http://127.0.0.1:8000/> Quit the server with CONTROL-C.
```

Ignorieren Sie die Warnung über unangewendete Datenbankmigrationen für jetzt; wir werden uns kurz mit der Datenbank befassen.

Sie haben den Django-Entwicklungsserver gestartet, einen leichtgewichtigen Webdienst, der ausschließlich in Python geschrieben ist. Wir haben ihn mit Django mitgeliefert, damit Sie Dinge schnell entwickeln können, ohne sich um die Konfiguration eines Produktionsservers wie Apache kümmern zu müssen, bis Sie für die Produktion bereit sind.

Jetzt ist ein guter Zeitpunkt, um zu beachten: **Verwenden Sie diesen Server nicht** in irgendeiner Weise, die einem Produktionsumfeld ähnelt. Er ist nur für die Entwicklung gedacht. (Wir sind im Geschäft von Webframeworks, nicht von Webdiensten.)

Jetzt, da der Server läuft, besuchen Sie <http://127.0.0.1:8000/> mit Ihrem Webbrowser. Oder führen Sie `curl 127.0.0.1:8000` in der Konsole aus. Sie werden eine Seite mit "Herzlichen Glückwunsch!" sehen, auf der ein Rakete abhebt. Es hat funktioniert!

In der LabEx VM müssen wir die LabEx-Domäne zu `ALLOWED_HOSTS` hinzufügen. Bearbeiten Sie `mysite/settings.py` und fügen Sie `*` am Ende von `ALLOWED_HOSTS` hinzu, so dass es wie folgt aussieht:

```python
ALLOWED_HOSTS = ["*"]
```

Dies sagt Django, dass es erlaubt ist, Anfragen mit beliebigen Host-Headern zu bedienen.

![Django development server running](../assets/20230907-08-56-33-3uvbOwp3.png)

## Ändern des Ports

Standardmäßig startet der Befehl `runserver` den Entwicklungsserver auf der internen IP und Port 8000.

Wenn Sie den Port des Servers ändern möchten, übergeben Sie ihn als Befehlszeilenargument. Beispielsweise startet dieser Befehl den Server auf Port 8080:

```bash
python manage.py runserver 8080
```

Wenn Sie die IP des Servers ändern möchten, übergeben Sie sie zusammen mit dem Port. Beispielsweise um auf alle verfügbaren öffentlichen IPs zu hören (was nützlich ist, wenn Sie Vagrant ausführen oder Ihre Arbeit auf anderen Computern im Netzwerk zeigen möchten), verwenden Sie:

```bash
python manage.py runserver 0.0.0.0:8080
```

Wechseln Sie jetzt in die Registerkarte **Web 8080** in der LabEx VM, und Sie werden die gleiche "Herzlichen Glückwunsch!"-Seite sehen.

![Django development server page](../assets/20230907-08-58-22-M3Luydxk.png)

Vollständige Dokumentation über den Entwicklungsserver finden Sie in der `runserver`-Referenz.

> Automatisches Neuladen von `runserver`
> Der Entwicklungsserver lädt Python-Code automatisch neu, wenn dies für jede Anfrage erforderlich ist. Sie müssen den Server nicht neu starten, damit Änderungen am Code wirksam werden. Einige Aktionen wie das Hinzufügen von Dateien lösen jedoch keinen Neustart aus, sodass Sie in diesen Fällen den Server neu starten müssen.
