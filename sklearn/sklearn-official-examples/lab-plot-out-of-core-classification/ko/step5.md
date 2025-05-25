# 미니배치 반복을 위한 생성자 함수 정의

```python
def iter_minibatches(doc_iter, minibatch_size):
    """미니배치 생성자."""
    X_text, y = get_minibatch(doc_iter, minibatch_size)
    while len(X_text):
        yield X_text, y
        X_text, y = get_minibatch(doc_iter, minibatch_size)
```
