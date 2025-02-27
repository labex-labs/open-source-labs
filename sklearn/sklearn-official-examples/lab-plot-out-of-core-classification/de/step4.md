# Definiere eine Funktion, um einen Minibatch von Beispielen zu erhalten

```python
def get_minibatch(doc_iter, size, pos_class=positive_class):
    """Extrahiere einen Minibatch von Beispielen, gib ein Tupel X_text, y zurück.

    Hinweis: size ist vor dem Ausschließen von ungültigen Dokumenten ohne zugewiesene Themen.

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
