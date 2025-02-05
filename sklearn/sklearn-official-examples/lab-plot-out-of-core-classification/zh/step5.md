# 定义一个生成器函数来遍历小批量数据

```python
def iter_minibatches(doc_iter, minibatch_size):
    """小批量数据的生成器。"""
    X_text, y = get_minibatch(doc_iter, minibatch_size)
    while len(X_text):
        yield X_text, y
        X_text, y = get_minibatch(doc_iter, minibatch_size)
```
