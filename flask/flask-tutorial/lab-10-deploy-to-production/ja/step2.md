# サーバーにアプリケーションをインストールする

wheel ファイルをサーバーにコピーします。サーバーにコピーしたら、新しい Python 仮想環境をセットアップし、pip を使って wheel ファイルをインストールします：

```bash
# Install the wheel file
pip install flaskr-1.0.0-py3-none-any.whl
```

これは新しい環境なので、データベースを再度初期化する必要があります：

```bash
# Initialize the database
flask --app flaskr init-db
```
