# Definindo uma View Assíncrona

No Flask, você pode definir views como funções assíncronas usando a sintaxe `async def`. Isso permite que você use `await` para realizar operações assíncronas dentro da função view.

```python
@app.route("/get-data")
async def get_data():
    data = await async_db_query(...)
    return jsonify(data)
```

Para executar este código, salve-o em um arquivo Python (por exemplo, `app.py`) e execute o arquivo usando o servidor de desenvolvimento Flask:

```bash
flask run
```
