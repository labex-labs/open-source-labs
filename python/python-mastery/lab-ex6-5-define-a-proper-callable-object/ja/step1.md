# 準備

演習4.3では、さまざまな種類の型と値のチェックを行うための一連の `Validator` クラスを作成しました。たとえば：

```python
>>> from validate import Integer
>>> Integer.check(1)
>>> Integer.check('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

このようにして、関数内でバリデータを使用することができます：

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>>
```

この演習では、もう少し進んでみましょう。
