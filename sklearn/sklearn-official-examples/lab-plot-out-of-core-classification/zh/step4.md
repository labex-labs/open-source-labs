# 定义一个函数来获取一批示例

```python
def get_minibatch(doc_iter, size, pos_class=positive_class):
    """提取一批示例，返回一个元组 X_text, y。

    注意：size 是在排除没有分配主题的无效文档之前的数量。

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
