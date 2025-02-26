# プログラムが失敗する方法

Pythonは、関数の引数の型や値のチェックや検証を行いません。関数は、関数内の文に対応する任意のデータで機能します。

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

関数にエラーがある場合、それらは実行時に例外として表示されます。

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

コードを検証するには、テスト（後述）に重点が置かれます。
