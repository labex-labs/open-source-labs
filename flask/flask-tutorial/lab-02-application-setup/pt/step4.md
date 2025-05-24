# Executando a Aplicação

Com sua aplicação configurada, você pode agora executá-la usando o comando `flask`. Certifique-se de executar este comando a partir do diretório de nível superior, não do pacote `flaskr`.

```bash
flask --app flaskr run --debug --host=0.0.0.0
```

Você deve ver uma saída semelhante a esta:

```bash
 * Serving Flask app "flaskr"
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

Em seguida, abra a aba **Web 5000**, e você deverá ver o seguinte:

![Flask app hello world page](../assets/hello-world.png)
