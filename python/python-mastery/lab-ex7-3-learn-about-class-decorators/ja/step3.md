# 継承によるデコレータの適用

ステップ 2 では、コードを簡素化するクラスデコレータを作成しました。クラスデコレータは、クラスを引数として受け取り、変更されたクラスを返す特別な種類の関数です。これは、元のコードを変更せずにクラスに機能を追加するための Python の便利なツールです。しかし、すべてのクラスに `@validate_attributes` デコレータを明示的に適用する必要があります。これは、検証が必要な新しいクラスを作成するたびに、このデコレータを追加することを覚えておく必要があることを意味し、これは少し面倒になる可能性があります。

継承を通じてデコレータを自動的に適用することで、これをさらに改善できます。継承は、サブクラスが親クラスから属性とメソッドを継承できるオブジェクト指向プログラミングの基本的な概念です。Python の `__init_subclass__` メソッドは Python 3.6 で導入され、親クラスがサブクラスの初期化をカスタマイズできるようにしました。これは、サブクラスが作成されると、親クラスがそれに何らかのアクションを実行できることを意味します。この機能を使用して、`Structure` を継承するすべてのクラスにデコレータを自動的に適用できます。

これを実装しましょう。

1. エディタで `structure.py` ファイルを開きます。このファイルには `Structure` クラスの定義が含まれており、`__init_subclass__` メソッドを使用するように変更します。

2. `Structure` クラスに `__init_subclass__` メソッドを追加します。

```python
class Structure:
    _fields = ()
    _types = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'

    @classmethod
    def create_init(cls):
        '''
        _fields から __init__ メソッドを作成します
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        # 関数作成コードを実行します
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

`__init_subclass__` メソッドはクラスメソッドであり、クラスのインスタンスではなくクラス自体で呼び出すことができます。`Structure` のサブクラスが作成されると、このメソッドが自動的に呼び出されます。このメソッド内で、サブクラス `cls` に対して `validate_attributes` デコレータを呼び出します。このようにして、`Structure` のすべてのサブクラスは自動的に検証動作を持つようになります。

3. ファイルを保存します。

`structure.py` ファイルに変更を加えたら、変更が適用されるように保存する必要があります。

4. それでは、この新機能を利用するように `stock.py` ファイルを更新しましょう。エディタで `stock.py` ファイルを開いて変更します。このファイルには `Stock` クラスの定義が含まれており、自動デコレータ適用を使用するために `Structure` クラスから継承するように変更します。

5. `stock.py` ファイルを変更して、明示的なデコレータを削除します。

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

以下の変更を行ったことに注意してください。

- デコレータは継承を通じて自動的に適用されるため、明示的にインポートする必要がなくなったため、`validate_attributes` のインポートを削除しました。
- `Structure` クラスの `__init_subclass__` メソッドが適用を処理するため、`@validate_attributes` デコレータを削除しました。
- コードは、検証動作を取得するために `Structure` からの継承のみに依存するようになりました。

6. すべてがまだ機能することを確認するために、再度テストを実行します。

```bash
cd ~/project
python3 teststock.py
```

テストを実行することは、変更によって何も壊れていないことを確認するために重要です。すべてのテストが合格した場合、それは継承による自動デコレータ適用が正しく機能していることを意味します。

すべてのテストが合格するはずです。

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Stock クラスを再度テストして、期待どおりに機能することを確認しましょう。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

このコマンドは `Stock` クラスのインスタンスを作成し、その表現とコストを出力します。出力が期待どおりであれば、`Stock` クラスが自動デコレータ適用で正しく機能していることを意味します。

出力：

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

この実装はさらにクリーンです！`__init_subclass__` を使用することで、デコレータを明示的に適用する必要がなくなりました。`Structure` を継承するすべてのクラスは、自動的に検証動作を取得します。
