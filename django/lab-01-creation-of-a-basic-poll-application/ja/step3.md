# 開発サーバー

Djangoプロジェクトが正常に動作することを確認しましょう。まだ行っていなければ、外側の `mysite` ディレクトリに移動して、次のコマンドを実行します。

```bash
cd ~/project/mysite
python manage.py runserver
```

コマンドラインに次の出力が表示されます。

```plaintext
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.

- 15:50:53 Django version, using settings'mysite.settings' Starting development server at <http://127.0.0.1:8000/> Quit the server with CONTROL-C.
```

まだ適用されていないデータベースマイグレーションに関する警告は今は無視してください。すぐ後でデータベースについて対処します。

Djangoの開発サーバーを起動しました。これは、純粋にPythonで書かれた軽量なWebサーバーです。Djangoにこれを含めたのは、本番環境用のサーバー（たとえばApache）を設定する面倒を省き、本番環境に備えるまで迅速に開発できるようにするためです。

ここで注意しておくことが重要です。**本番環境に似た環境ではこのサーバーを使わないでください**。これは開発中にのみ使用することを想定しています。（私たちはWebフレームワークを作るビジネスをしているので、Webサーバーは作っていません。）

サーバーが起動したら、Webブラウザで <http://127.0.0.1:8000/> にアクセスしてください。または、ターミナルで `curl 127.0.0.1:8000` を実行しても良いです。「おめでとうございます！」というページが表示され、ロケットが打ち上がっているはずです。成功です！

LabEx VMでは、LabExドメインを `ALLOWED_HOSTS` に追加する必要があります。`mysite/settings.py` を編集して、`ALLOWED_HOSTS` の末尾に `*` を追加します。このようになります。

```python
ALLOWED_HOSTS = ["*"]
```

これにより、Djangoに任意のホストヘッダーでリクエストを処理することが許可されるようになります。

![Django development server running](../assets/20230907-08-56-33-3uvbOwp3.png)

## ポートの変更

デフォルトでは、`runserver` コマンドは内部IPのポート8000で開発サーバーを起動します。

サーバーのポートを変更したい場合は、コマンドライン引数として指定します。たとえば、このコマンドはポート8080でサーバーを起動します。

```bash
python manage.py runserver 8080
```

サーバーのIPを変更したい場合は、ポートと一緒に指定します。たとえば、すべての利用可能なパブリックIPでリッスンするには（Vagrantを実行している場合や、ネットワーク上の他のコンピュータで作業成果を見せたい場合に便利）、次のように使用します。

```bash
python manage.py runserver 0.0.0.0:8080
```

次に、LabEx VMの **Web 8080** タブに切り替えると、同じ「おめでとう」ページが表示されます。

![Django development server page](../assets/20230907-08-58-22-M3Luydxk.png)

開発サーバーの完全なドキュメントは、`runserver` のリファレンスで見つけることができます。

> `runserver` の自動リロード
> 開発サーバーは、必要に応じて各リクエストごとにPythonコードを自動的に再読み込みします。コードの変更が反映されるようにサーバーを再起動する必要はありません。ただし、ファイルの追加などの一部の操作は再起動をトリガーしません。この場合、サーバーを再起動する必要があります。
