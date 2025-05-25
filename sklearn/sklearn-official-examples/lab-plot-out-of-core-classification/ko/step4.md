# 예제 미니배치를 가져오는 함수 정의

```python
def get_minibatch(doc_iter, size, pos_class=positive_class):
    """예제의 미니배치를 추출하고, 튜플 X_text, y 를 반환합니다.

    참고: 크기는 할당된 주제가 없는 유효하지 않은 문서를 제외하기 전의 크기입니다.

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
