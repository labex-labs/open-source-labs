# Defining an Async View

In Flask, you can define views as asynchronous functions using the `async def` syntax. This allows you to use `await` to perform asynchronous operations within the view function.

```python
@app.route("/get-data")
async def get_data():
    data = await async_db_query(...)
    return jsonify(data)
```

To run this code, save it in a Python file (e.g., `app.py`) and execute the file using the Flask development server:

```bash
flask run
```
