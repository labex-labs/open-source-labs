# Définition d'une vue asynchrone

Dans Flask, vous pouvez définir des vues comme des fonctions asynchrones en utilisant la syntaxe `async def`. Cela vous permet d'utiliser `await` pour effectuer des opérations asynchrones à l'intérieur de la fonction de vue.

```python
@app.route("/get-data")
async def get_data():
    data = await async_db_query(...)
    return jsonify(data)
```

Pour exécuter ce code, enregistrez-le dans un fichier Python (par exemple, `app.py`) et exécutez le fichier à l'aide du serveur de développement Flask :

```bash
flask run
```
