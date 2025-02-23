# Definiendo una vista asincrónica

En Flask, puedes definir vistas como funciones asincrónicas utilizando la sintaxis `async def`. Esto te permite utilizar `await` para realizar operaciones asincrónicas dentro de la función de vista.

```python
@app.route("/get-data")
async def get_data():
    data = await async_db_query(...)
    return jsonify(data)
```

Para ejecutar este código, guárdalo en un archivo de Python (por ejemplo, `app.py`) y ejecuta el archivo utilizando el servidor de desarrollo de Flask:

```bash
flask run
```
