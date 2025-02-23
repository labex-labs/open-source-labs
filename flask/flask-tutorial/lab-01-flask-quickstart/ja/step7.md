# 再度アプリケーションを実行する

再度アプリケーションを実行して、動的コンテンツ機能をテストしましょう。

1. Flask 開発サーバーがまだ実行中であれば停止します（Ctrl+C を押します）。
2. 以下のコマンドを実行してサーバーを再度起動します。

   ```bash
   flask run --host=0.0.0.0
   ```

3. **Web 5000** のタブの URL をコピーし、ブラウザの新しいタブに貼り付けます。

![Copying Web 5000 URL](../assets/copy-url.png)

4. URL の末尾に `/LabEx` を追加して Enter キーを押します。

![Hello LabEx webpage](../assets/hello-labex.png)

5. URL 内の `name` パラメータの値を変更して Enter キーを押します。
