# 定义异步视图

在 Flask 中，你可以使用 `async def` 语法将视图定义为异步函数。这使你能够在视图函数中使用 `await` 来执行异步操作。

```python
@app.route("/get-data")
async def get_data():
    data = await async_db_query(...)
    return jsonify(data)
```

要运行此代码，请将其保存在 Python 文件（例如 `app.py`）中，并使用 Flask 开发服务器执行该文件：

```bash
flask run
```
