# ミニバッチを反復処理するためのジェネレータ関数を定義する

```python
def iter_minibatches(doc_iter, minibatch_size):
    """ミニバッチのジェネレータ。"""
    X_text, y = get_minibatch(doc_iter, minibatch_size)
    while len(X_text):
        yield X_text, y
        X_text, y = get_minibatch(doc_iter, minibatch_size)
```
