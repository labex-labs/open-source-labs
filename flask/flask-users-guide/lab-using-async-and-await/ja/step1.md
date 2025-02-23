# 非同期ビューの定義

Flaskでは、`async def`構文を使用してビューを非同期関数として定義できます。これにより、ビュー関数内で`await`を使用して非同期操作を実行できるようになります。

```python
@app.route("/get-data")
async def get_data():
    data = await async_db_query(...)
    return jsonify(data)
```

このコードを実行するには、Pythonファイル（たとえば`app.py`）に保存し、Flask開発サーバーを使用してファイルを実行します。

```bash
flask run
```
