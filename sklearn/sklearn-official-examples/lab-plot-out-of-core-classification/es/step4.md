# Definir una función para obtener un lote pequeño de ejemplos

```python
def get_minibatch(doc_iter, size, pos_class=positive_class):
    """Extraer un lote pequeño de ejemplos, devolver una tupla X_text, y.

    Nota: size es antes de excluir los documentos no válidos sin temas asignados.

    """
    data = [
        ("{title}\n\n{body}".format(**doc), pos_class in doc["topics"])
        for doc in itertools.islice(doc_iter, size)
        if doc["topics"]
    ]
    if not len(data):
        return np.asarray([], dtype=int), np.asarray([], dtype=int)
    X_text, y = zip(*data)
    return X_text, np.asarray(y, dtype=int)
```
