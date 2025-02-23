# Tests schreiben

Jetzt, nachdem du die Testumgebung eingerichtet hast, kannst du mit dem Schreiben von Tests für deine Flask-Anwendung beginnen. Hier sind einige Beispiele für häufige Tests, die du möglicherweise schreiben möchtest:

1. Einen Route testen:

   ```python
   def test_hello(client):
       response = client.get("/")
       assert response.status_code == 200
       assert b"Hello, World!" in response.data
   ```

   Dieser Test sendet einen GET-Anfrage an die Wurzelroute ("/") und überprüft, dass der Antwortstatuscode 200 ist und die Antwortdaten den String "Hello, World!" enthalten.

2. Einen POST-Anfrage testen:

   ```python
   def test_login(client):
       response = client.post("/login", data={"username": "test", "password": "pass"})
       assert response.status_code == 200
       assert b"Logged in successfully" in response.data
   ```

   Dieser Test sendet eine POST-Anfrage an die Login-Route ("/login") mit Formulardaten, die einen Benutzernamen und ein Passwort enthalten. Es wird überprüft, dass der Antwortstatuscode 200 ist und die Antwortdaten den String "Logged in successfully" enthalten.

3. Einen Befehl testen:

   ```python
   def test_hello_command(runner):
       result = runner.invoke(args=["hello"])
       assert result.exit_code == 0
       assert "Hello, World!" in result.output
   ```

   Dieser Test ruft einen Befehl namens "hello" auf und überprüft, dass der Befehl mit einem Exit-Code von 0 beendet wird und die Ausgabe den String "Hello, World!" enthält.
