# 新しいメソッドの追加

株式数を減らすことで一定数の株を売却する`sell(nshares)`という新しいメソッドをStockに追加します。以下のように動作させます。

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>>
```

## 注:

`stock.py`ファイル内の`sell(nshares)`関数を完成させます。
