# Flask einrichten

Um mit Flask zu beginnen, müssen Sie es installieren und ein neues Projekt einrichten. Befolgen Sie die folgenden Anweisungen:

1. Installieren Sie Flask, indem Sie den folgenden Befehl in Ihrem Terminal oder der Befehlszeile ausführen:

   ```bash
   pip install flask
   ```

2. Öffnen Sie eine neue Datei und speichern Sie sie als `app.py`.

   ```bash
   cd ~/project
   touch app.py
   ```

3. Importieren Sie das Flask-Modul und erstellen Sie eine Instanz der Flask-Klasse:

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```
