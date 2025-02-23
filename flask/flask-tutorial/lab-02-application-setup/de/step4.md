# Ausführen der Anwendung

Wenn Ihre Anwendung eingerichtet und konfiguriert ist, können Sie sie nun mit dem Befehl `flask` ausführen. Stellen Sie sicher, dass Sie diesen Befehl aus dem obersten Verzeichnis ausführen, nicht aus dem Paket `flaskr`.

```bash
flask --app flaskr run --debug --host=0.0.0.0
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```bash
 * Serving Flask app "flaskr"
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

Öffnen Sie dann die Registerkarte **Web 5000**, und Sie sollten Folgendes sehen:

![Flask app hello world page](../assets/hello-world.png)
