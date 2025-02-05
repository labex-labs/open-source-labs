# 创建发射器函数

发射器函数生成将被传递到更新方法的数据。在这种情况下，我们以 0.1 的概率生成随机数据。

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```
