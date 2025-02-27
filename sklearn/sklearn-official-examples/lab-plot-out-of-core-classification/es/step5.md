# Definir una función generadora para iterar sobre lotes pequeños

```python
def iter_minibatches(doc_iter, minibatch_size):
    """Generador de lotes pequeños."""
    X_text, y = get_minibatch(doc_iter, minibatch_size)
    while len(X_text):
        yield X_text, y
        X_text, y = get_minibatch(doc_iter, minibatch_size)
```
