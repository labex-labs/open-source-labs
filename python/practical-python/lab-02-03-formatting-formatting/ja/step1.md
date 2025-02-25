# 文字列の書式設定

Python 3.6以降で文字列を書式設定する方法の1つは、`f-文字列`を使うことです。

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
>>>
```

`{式:書式}`の部分が置き換えられます。

これは一般的に`print`とともに使用されます。

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```
