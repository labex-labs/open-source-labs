# 本番サーバーでアプリケーションを実行する

本番環境では、組み込みの開発サーバーの代わりに WSGI サーバーを使用する必要があります。私たちは Waitress を WSGI サーバーとして使用します。

まず、Waitress をインストールします：

```bash
# Install Waitress
pip install waitress
```

次に、Waitress にアプリケーションをサービスするように指示します：

```bash
# Run the application with Waitress
waitress-serve --call 'flaskr:create_app'
```
