# まとめる

演習6.1では、汎用的な `__init__()`、`__setattr__()`、および `__repr__()` メソッドを定義する `Structure` クラスを作成しました。このクラスでは、ユーザーが次のように `_fields` クラス変数を定義する必要がありました：

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

このクラスの問題は、`__init__()` 関数がヘルプやキーワード引数の渡し方の目的では有用な引数シグネチャを持っていないことです。演習6.2では、特殊な `self._init()` 関数を使ったずるいトリックをしました。たとえば：

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')
    def __init__(self, name, shares, price):
        self._init()
  ...
```

これは有用なシグネチャを与えますが、ユーザーが `_fields` 変数と `__init__()` メソッドの両方を提供しなければならないため、今のクラスは奇妙になっています。

あなたの課題は、いくつかの関数検査技術を使って `_fields` 変数を排除することです。まず、`Stock` から引数シグネチャを次のように取得できることに注意してください：

```python
>>> import inspect
>>> sig = inspect.signature(Stock)
>>> tuple(sig.parameters)
('name','shares', 'price')
>>>
```

おそらく、`__init__()` の引数シグネチャから `_fields` 変数を設定できるでしょう。`Structure` に `set_fields(cls)` というクラスメソッドを追加して、`__init__()` 関数を検査し、`_fields` 変数を適切に設定します。新しい関数を次のように使うはずです：

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

  ...

Stock.set_fields()
```

結果として得られるクラスは、以前と同じように機能するはずです：

```python
>>> s = Stock(name='GOOG', shares=100, price=490.1)
>>> s
Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 12, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>>
```

再び単体テストで少し修正した `Stock` クラスを検証してください。まだ失敗はありますが、前の演習と比べて何も変化しないはずです。

この時点では、まだ少し「こじつけ」な感じがしますが、進歩しています。役に立つ `__init__()` 関数を持つ `Stock` 構造体クラスがあり、役に立つ表現文字列があり、`__setattr__()` メソッドが属性名のセットを制限しています。`set_fields()` を呼び出さなければならないという追加のステップは少し奇妙ですが、それについては後で戻ります。
