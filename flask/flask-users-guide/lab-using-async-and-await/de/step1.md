# Definieren einer asynchronen Ansicht

In Flask können Sie Ansichten als asynchrone Funktionen mit der `async def`-Syntax definieren. Dadurch können Sie `await` verwenden, um asynchrone Operationen innerhalb der Ansichtsfunktion durchzuführen.

```python
@app.route("/get-data")
async def get_data():
    data = await async_db_query(...)
    return jsonify(data)
```

Um diesen Code auszuführen, speichern Sie ihn in einer Python-Datei (z. B. `app.py`) und führen Sie die Datei mit dem Flask-Entwicklungsserver aus:

```bash
flask run
```
