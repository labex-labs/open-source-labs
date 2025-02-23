# Installieren Sie die Anwendung auf dem Server

Kopieren Sie die Wheel-Datei auf Ihren Server. Wenn Sie die Datei dort haben, erstellen Sie eine neue Python-Virtual-Umgebung und installieren Sie die Wheel-Datei mit pip:

```bash
# Installieren Sie die Wheel-Datei
pip install flaskr-1.0.0-py3-none-any.whl
```

Da dies eine neue Umgebung ist, müssen Sie die Datenbank erneut initialisieren:

```bash
# Initialisieren Sie die Datenbank
flask --app flaskr init-db
```
