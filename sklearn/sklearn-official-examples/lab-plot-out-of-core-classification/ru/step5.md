# Определяем генераторную функцию для перебора мини - пакетов

```python
def iter_minibatches(doc_iter, minibatch_size):
    """Генератор мини - пакетов."""
    X_text, y = get_minibatch(doc_iter, minibatch_size)
    while len(X_text):
        yield X_text, y
        X_text, y = get_minibatch(doc_iter, minibatch_size)
```
