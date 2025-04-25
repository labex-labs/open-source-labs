# メソッド呼び出し

メソッドを呼び出すには 2 段階のプロセスが必要です。

1.  検索：`.` 演算子
2.  メソッド呼び出し：`()` 演算子

```python
>>> s = stock.Stock('GOOG',100,490.10)
>>> c = s.cost  # 検索
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()         # メソッド呼び出し
49010.0
>>>
```
