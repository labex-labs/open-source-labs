# すべてはオブジェクト

数値、文字列、リスト、関数、例外、クラス、インスタンスなどはすべてオブジェクトです。これは、名前を付けることができるすべてのオブジェクトが、制限なくデータとして渡され、コンテナに配置されるなどということを意味します。特別な種類のオブジェクトはありません。時には、すべてのオブジェクトが「一等公民」であると言われます。

簡単な例:

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<built-in function abs>,
  <module'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Failed!')
Failed!
>>>
```

ここで、`items` は関数、モジュール、例外を含むリストです。リスト内の要素を元の名前の代わりに直接使用できます:

```python
items[0](-45)       # abs
items[1].sqrt(2)    # math
except items[2]:    # ValueError
```

力は責任を伴います。それができるからといって、やるべきだというわけではありません。

このセットの演習では、一等公民オブジェクトから生じる力のいくつかを見てみましょう。
