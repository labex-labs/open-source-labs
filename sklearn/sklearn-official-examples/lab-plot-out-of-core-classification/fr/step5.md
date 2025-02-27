# Définir une fonction génératrice pour itérer sur les mini-lots

```python
def iter_minibatches(doc_iter, minibatch_size):
    """Générateur de mini-lots."""
    X_text, y = get_minibatch(doc_iter, minibatch_size)
    while len(X_text):
        yield X_text, y
        X_text, y = get_minibatch(doc_iter, minibatch_size)
```
