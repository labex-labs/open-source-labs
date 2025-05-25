# Definir uma função geradora para iterar sobre minilotes

```python
def iter_minibatches(doc_iter, minibatch_size):
    """Gerador de minilotes."""
    X_text, y = get_minibatch(doc_iter, minibatch_size)
    while len(X_text):
        yield X_text, y
        X_text, y = get_minibatch(doc_iter, minibatch_size)
```
