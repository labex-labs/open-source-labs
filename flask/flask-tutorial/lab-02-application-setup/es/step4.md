# Ejecutando la aplicación

Con tu aplicación configurada, ahora puedes ejecutarla usando el comando `flask`. Asegúrate de ejecutar este comando desde el directorio principal, no desde el paquete `flaskr`.

```bash
flask --app flaskr run --debug --host=0.0.0.0
```

Deberías ver una salida similar a esta:

```bash
 * Serving Flask app "flaskr"
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

Luego, abre la pestaña **Web 5000**, y deberías ver lo siguiente:

![Flask app hello world page](../assets/hello-world.png)
