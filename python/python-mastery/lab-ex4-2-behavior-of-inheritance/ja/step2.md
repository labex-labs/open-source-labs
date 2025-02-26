# 値チェッカーを作成する

演習 3.4 では、`Stock` クラスに、異なる型と値の属性をチェックするいくつかのプロパティを追加しました（たとえば、株式数は正の整数でなければなりません）。この考え方を少し遊んでみましょう。まず、`validate.py` というファイルを作成し、次の基底クラスを定義します。

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

次に、型チェック用のいくつかのクラスを作成しましょう。

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

これらのクラスの使い方は次のとおりです（注：`@classmethod` を使うことで、実際に必要ないインスタンスを作成する余分な手順を回避できます）。

```python
>>> Integer.check(10)
10
>>> Integer.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>> String.check('10')
'10'
>>>
```

関数でバリデータを使うこともできます。たとえば：

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>> add(2, 2)
4
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in add
  File "validate.py", line 11, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

次に、さまざまな種類のドメインチェック用のクラスをいくつか作成しましょう。

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

これらは何のために作られるのでしょうか？ 次のように、多重継承を使ってクラスを組み合わせていきましょう。これはおもちゃのブロックのようにです。

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

基本的には、既存のバリデータを取り出して、新しいバリデータに組み合わせています。狂気です！ では、今度はこれらを使って何かを検証してみましょう。

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>> PositiveInteger.check(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('Expected >= 0')
ValueError: Must be >= 0


>>> NonEmptyString.check('hello')
'hello'
>>> NonEmptyString.check('')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('Must be non-empty')
ValueError: Must be non-empty
>>>
```

この時点では、おそらくあなたの頭は完全に爆発しているでしょう。しかし、さまざまなコードの断片を組み合わせる問題は、現実世界のプログラムでも起こります。協調的な多重継承は、それを整理するために使えるツールの 1 つです。
