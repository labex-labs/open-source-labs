# 継承を通じたデコレータの適用

ステップ2では、コードを簡素化するクラスデコレータを作成しました。クラスデコレータは、クラスを引数として受け取り、変更されたクラスを返す特殊な関数です。Pythonでは、クラスの元のコードを変更せずに機能を追加するための便利なツールです。しかし、依然として `@validate_attributes` デコレータを各クラスに明示的に適用する必要があります。これは、検証が必要な新しいクラスを作成するたびに、このデコレータを追加することを忘れないようにする必要があり、少し面倒です。

これをさらに改善するために、継承を通じてデコレータを自動的に適用することができます。継承は、オブジェクト指向プログラミングの基本的な概念で、サブクラスはスーパークラスから属性とメソッドを継承することができます。Python 3.6で導入された `__init_subclass__` メソッドは、スーパークラスがサブクラスの初期化をカスタマイズできるようにするためのものです。つまり、サブクラスが作成されると、スーパークラスはそれに対していくつかのアクションを実行することができます。この機能を使用して、`Structure` から継承するすべてのクラスに自動的にデコレータを適用することができます。

これを実装してみましょう。

1. `structure.py` ファイルを開きます。

```bash
code ~/project/structure.py
```

ここでは、`code` コマンドを使用して、コードエディタで `structure.py` ファイルを開いています。このファイルには `Structure` クラスの定義が含まれており、`__init_subclass__` メソッドを使用するように変更します。

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
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        # Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

`__init_subclass__` メソッドはクラスメソッドです。つまり、クラスのインスタンスではなく、クラス自体に対して呼び出すことができます。`Structure` のサブクラスが作成されると、このメソッドは自動的に呼び出されます。このメソッドの中で、サブクラス `cls` に対して `validate_attributes` デコレータを呼び出します。このようにして、`Structure` のすべてのサブクラスは自動的に検証機能を持つことになります。

3. ファイルを保存します。

`structure.py` ファイルに変更を加えた後、変更が適用されるようにファイルを保存する必要があります。

4. この新機能を利用するために、`stock.py` ファイルを更新しましょう。

```bash
code ~/project/stock.py
```

`stock.py` ファイルを開いて変更します。このファイルには `Stock` クラスの定義が含まれており、自動的なデコレータの適用を利用するために `Structure` クラスから継承するように変更します。

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

以下の点に注意してください。

- `validate_attributes` のインポートを削除しました。なぜなら、継承を通じてデコレータが自動的に適用されるため、明示的にインポートする必要がなくなったからです。
- `@validate_attributes` デコレータを削除しました。なぜなら、`Structure` クラスの `__init_subclass__` メソッドがその適用を担当するからです。
- これで、コードは `Structure` からの継承にのみ依存して検証機能を取得するようになりました。

6. すべてが正常に動作することを確認するために、再度テストを実行します。

```bash
cd ~/project
python3 teststock.py
```

テストを実行することは、変更によって何かが壊れていないことを確認するために重要です。すべてのテストが合格すれば、継承を通じた自動的なデコレータの適用が正しく機能していることを意味します。

すべてのテストが合格するはずです。

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

`Stock` クラスが期待通りに動作することを確認するために、もう一度テストしてみましょう。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

このコマンドは `Stock` クラスのインスタンスを作成し、その表現とコストを印刷します。出力が期待通りであれば、自動的なデコレータの適用で `Stock` クラスが正しく動作していることを意味します。

出力:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

この実装はさらにクリーンです！`__init_subclass__` を使用することで、明示的にデコレータを適用する必要がなくなりました。`Structure` から継承するすべてのクラスは自動的に検証機能を持つようになります。
