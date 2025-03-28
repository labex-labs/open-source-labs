# アプリケーションの実行

これで Flask アプリケーションをセットアップし、基本的なルートを作成しましたので、アプリケーションを実行して動作を確認しましょう。

1. ターミナルまたはコマンドプロンプトで、`app.py` ファイルがあるディレクトリに移動します。
2. 以下のコマンドを実行して Flask 開発サーバーを起動します。

   ```bash
   flask run --host=0.0.0.0
   ```

`--host=0.0.0.0` は、アプリケーションを公開で利用可能にするために使用されます。これを指定しない場合、アプリケーションはローカルマシン上でのみ利用可能になります。

その後、**Web 5000** のタブに切り替えてページを更新します。
