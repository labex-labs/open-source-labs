# Python から開発サーバを実行する

Flask CLI コマンドを使用する以外にも、Python コードから開発サーバを起動することもできます。`app.py` ファイルの末尾に次のコードを追加します。

```python
if __name__ == "__main__":
    app.run(debug=True)
```

これで、`app.py` ファイルを Python で実行することで開発サーバを起動できます。

```bash
python app.py
```

これにより開発サーバが起動し、以前と同じ方法で Flask アプリケーションにアクセスできます。
