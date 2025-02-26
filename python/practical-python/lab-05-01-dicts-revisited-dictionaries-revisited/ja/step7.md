# インスタンスの変更

オブジェクトを変更する操作は、その下にある辞書を更新します。

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name':'GOOG','shares': 100, 'price': 490.1 }
>>> s.shares = 50       # 設定
>>> s.date = '6/7/2007' # 設定
>>> s.__dict__
{ 'name': 'GOOG','shares': 50, 'price': 490.1, 'date': '6/7/2007' }
>>> del s.shares        # 削除
>>> s.__dict__
{ 'name': 'GOOG', 'price': 490.1, 'date': '6/7/2007' }
>>>
```
