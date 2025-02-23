# Testumgebung einrichten

Bevor du mit dem Schreiben von Tests für deine Flask-Anwendung beginnen kannst, musst du die Testumgebung einrichten. Hier sind die Schritte dazu:

1. Installiere das `pytest`-Framework, indem du folgenden Befehl ausführst:

   ```bash
   pip install pytest
   ```

2. Erstelle in einem Ordner namens `tests` deiner Flask-Anwendung eine neue Datei namens `conftest.py`.

3. Importiere in der Datei `conftest.py` die erforderlichen Module:

   ```python
   import pytest
   from my_app import create_app
   ```

4. Definiere einen Fixture namens `app`, der eine App-Instanz erstellt und konfiguriert:

   ```python
   @pytest.fixture()
   def app():
       app = create_app()
       app.config.update({
           "TESTING": True,
       })
       yield app
   ```

   Beachte, dass du den Fixture entsprechend anpassen solltest, wenn du das Anwendungsfactory-Pattern verwendest.

5. Definiere Fixtures für den Testclient und den CLI-Laufenden:

   ```python
   @pytest.fixture()
   def client(app):
       return app.test_client()

   @pytest.fixture()
   def runner(app):
       return app.test_cli_runner()
   ```
