# 配置密钥

在生产环境中，你应该将密钥更改为一个随机值。要生成一个随机密钥，请运行以下命令：

```bash
# 生成一个随机密钥
python -c 'import secrets; print(secrets.token_hex())'
```

在实例文件夹中创建一个`config.py`文件，并将`SECRET_KEY`设置为生成的值。

```python
#.venv/var/flaskr-instance/config.py

SECRET_KEY = 'your_generated_secret_key'
```
