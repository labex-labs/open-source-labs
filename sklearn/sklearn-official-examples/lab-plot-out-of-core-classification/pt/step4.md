# Definir uma função para obter um mini lote de exemplos

```python
def get_minibatch(doc_iter, size, pos_class=positive_class):
    """Extrair um mini lote de exemplos, retornar uma tupla X_text, y.

    Nota: o tamanho é antes de excluir documentos inválidos sem tópicos atribuídos.

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
