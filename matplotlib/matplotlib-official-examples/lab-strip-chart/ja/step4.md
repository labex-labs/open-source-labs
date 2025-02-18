# エミッター関数の作成

エミッター関数は、更新メソッドに渡されるデータを生成します。この場合、確率 0.1 でランダムなデータを生成します。

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```
