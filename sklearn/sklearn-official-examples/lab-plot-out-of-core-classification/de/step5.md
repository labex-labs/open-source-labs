# Definiere eine Generatorfunktion, um über Minibatches zu iterieren

```python
def iter_minibatches(doc_iter, minibatch_size):
    """Generator von Minibatches."""
    X_text, y = get_minibatch(doc_iter, minibatch_size)
    while len(X_text):
        yield X_text, y
        X_text, y = get_minibatch(doc_iter, minibatch_size)
```
