# 再度アプリケーションを実行する

これで HTML テンプレートを追加したので、再度アプリケーションを実行してレンダリングされたテンプレートを見てみましょう。

1. Flask 開発サーバーがまだ実行中であれば停止します（Ctrl+C を押します）。
2. 以下のコマンドを実行してサーバーを再度起動します。

   ```bash
   flask run --host=0.0.0.0
   ```

このとき、HTML テンプレートに「Hello, Flask!」のメッセージが表示されるはずです。

![Hello, Flask!](../assets/hello-flask.png)
