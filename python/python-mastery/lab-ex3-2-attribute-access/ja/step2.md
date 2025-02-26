# getattr() の使用

`getattr()` 関数は、オブジェクトを非常に汎用的に処理するコードを書く際に非常に便利です。例を挙げると、ユーザ定義の属性のセットを出力するこの例を考えてみてください。

```python
>>> s= Stock('GOOG', 100, 490.1)
>>> fields = ['name','shares','price']
>>> for name in fields:
           print(name, getattr(s, name))

name GOOG
shares 100
price 490.1
>>>
```
