# Определяем функцию для получения мини - пакета примеров

```python
def get_minibatch(doc_iter, size, pos_class=positive_class):
    """Извлекает мини - пакет примеров, возвращает кортеж X_text, y.

    Примечание: размер указывается до исключения недействительных документов без назначенных тем.

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
