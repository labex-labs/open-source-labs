# サーバーにアプリケーションをインストールする

wheelファイルをサーバーにコピーします。サーバーにコピーしたら、新しいPython仮想環境をセットアップし、pipを使ってwheelファイルをインストールします：

```bash
# Install the wheel file
pip install flaskr-1.0.0-py3-none-any.whl
```

これは新しい環境なので、データベースを再度初期化する必要があります：

```bash
# Initialize the database
flask --app flaskr init-db
```
