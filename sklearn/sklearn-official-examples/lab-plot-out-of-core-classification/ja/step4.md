# サンプルのミニバッチを取得する関数を定義する

```python
def get_minibatch(doc_iter, size, pos_class=positive_class):
    """サンプルのミニバッチを抽出し、タプル X_text, y を返す。

    注：サイズは、割り当てられていないトピックがない無効な文書を除外する前のものである。

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
