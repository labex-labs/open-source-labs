# 本番サーバーでアプリケーションを実行する

本番環境では、組み込みの開発サーバーの代わりにWSGIサーバーを使用する必要があります。私たちはWaitressをWSGIサーバーとして使用します。

まず、Waitressをインストールします：

```bash
# Install Waitress
pip install waitress
```

次に、Waitressにアプリケーションをサービスするように指示します：

```bash
# Run the application with Waitress
waitress-serve --call 'flaskr:create_app'
```
