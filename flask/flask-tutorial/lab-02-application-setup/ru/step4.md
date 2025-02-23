# Запуск приложения

После настройки и настройки вашего приложения вы можете теперь запустить его с помощью команды `flask`. Убедитесь, что запускаете эту команду из верхнего уровня директории, а не из пакета `flaskr`.

```bash
flask --app flaskr run --debug --host=0.0.0.0
```

Вы должны увидеть вывод, похожий на этот:

```bash
 * Serving Flask app "flaskr"
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

Затем откройте вкладку **Web 5000**, и вы должны увидеть следующее:

![Flask app hello world page](../assets/hello-world.png)
