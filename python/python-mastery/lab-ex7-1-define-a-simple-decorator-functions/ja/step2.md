# 本格的なデコレータ

ヒント: `validate.py` ファイルで次のことを行います。

演習6.6では、型アノテーションを強制するコール可能なクラス `ValidatedFunction` を作成しました。このクラスを `validated` と呼ばれるデコレータ関数に書き換えます。これにより、次のようなコードを書けるようになります。

```python
from validate import Integer, validated

@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y:Integer) -> Integer:
    return x ** y
```

デコレートされた関数の動作方法は次のとおりです。

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>

>>> pow(2, 3)
8
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
```

デコレータは例外を修正して、より有用な情報を表示するようにします。また、`@validated` デコレータはクラスでも機能する必要があります(特別なことは何もしなくてもよい)。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares:PositiveInteger):
        self.shares -= nshares
```

注: この部分はコード量が多くありませんが、細かい部分がたくさんあります。解決策は演習6.6とほぼ同じになります。ただし、解決策のコードを見るのは恥ずかしがらないでください。
