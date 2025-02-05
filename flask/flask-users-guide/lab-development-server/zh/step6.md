# 从 Python 运行开发服务器

除了使用 Flask CLI 命令外，你还可以从 Python 代码启动开发服务器。在你的 `app.py` 文件末尾添加以下代码：

```python
if __name__ == "__main__":
    app.run(debug=True)
```

现在，你可以通过使用 Python 执行 `app.py` 文件来运行开发服务器：

```bash
python app.py
```

这将启动开发服务器，并且你可以像之前一样访问你的 Flask 应用程序。
