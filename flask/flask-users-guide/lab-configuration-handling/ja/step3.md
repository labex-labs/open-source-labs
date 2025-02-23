# ファイルからの設定

コード内に設定値をハードコーディングするのは理想的ではありません。特に機密情報の場合には。Flask は、別のファイルから設定を読み込む方法を提供しています。`config.py` という名前の新しいファイルを作成し、次のコードを追加します。

```python
DEBUG = False
SECRET_KEY ='myothersecretkey'
```

`app.py` ファイルで、以前の設定コードを次のものに置き換えます。

```python
app.config.from_object('config')
```

`from_object` メソッドは、`config` モジュールから設定を読み込みます。これで、`DEBUG` と `SECRET_KEY` の値が `config.py` ファイルから読み込まれるようになります。

Flask アプリケーションを再起動し、`http://localhost:5000` にアクセスして、新しい設定値付きの更新されたメッセージを表示します。
