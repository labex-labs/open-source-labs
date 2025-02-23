# アプリケーションの実行

アプリケーションをセットアップして構成したので、今では `flask` コマンドを使って実行できます。このコマンドは、トップレベルのディレクトリから実行すること、`flaskr` パッケージからではないことに注意してください。

```bash
flask --app flaskr run --debug --host=0.0.0.0
```

以下のような出力が表示されるはずです。

```bash
 * Serving Flask app "flaskr"
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

次に、**Web 5000** のタブを開き、以下のように表示されるはずです。

![Flask app hello world page](../assets/hello-world.png)
