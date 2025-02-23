# シークレットキーの設定

本番環境では、シークレットキーをランダムな値に変更する必要があります。ランダムなシークレットキーを生成するには、次のコマンドを実行します：

```bash
# Generate a random secret key
python -c 'import secrets; print(secrets.token_hex())'
```

インスタンスフォルダに`config.py`ファイルを作成し、`SECRET_KEY`を生成した値に設定します。

```python
#.venv/var/flaskr-instance/config.py

SECRET_KEY = 'your_generated_secret_key'
```
