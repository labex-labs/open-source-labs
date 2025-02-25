# 演習1.17：f文字列

時には、文字列を作成してその中に変数の値を埋め込みたい場合があります。

そのためには、f文字列（f-string）を使います。たとえば：

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} shares of {name} at ${price:0.2f}'
'100 shares of IBM at $91.10'
>>>
```

演習1.10の `mortgage.py` プログラムを変更して、f文字列（f-string）を使ってその出力を作成してください。出力がきれいに整列するようにしてみてください。
