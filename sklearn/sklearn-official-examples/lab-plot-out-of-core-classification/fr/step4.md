# Définir une fonction pour obtenir un mini-lot d'exemples

```python
def get_minibatch(doc_iter, size, pos_class=positive_class):
    """Extraire un mini-lot d'exemples, retourner un tuple X_text, y.

    Note : size est avant d'exclure les documents invalides sans sujets assignés.

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
