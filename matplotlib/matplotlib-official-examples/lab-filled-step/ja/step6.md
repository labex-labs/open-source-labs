# 乱数データを生成する

`numpy.random.randn` を使って乱数データを生成します。12250個のポイントからなる4セットのデータを生成します。

```python
np.random.seed(19680801)
stack_data = np.random.randn(4, 12250)
```
