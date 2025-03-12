# StructureMeta メタクラスの作成

では、次に行うことについて話しましょう。すべてのバリデータ型を収集する方法を見つけました。次のステップはメタクラスを作成することです。では、メタクラスとは具体的に何でしょうか？Python では、メタクラスは特殊な種類のクラスです。そのインスタンスはクラス自体です。つまり、メタクラスはクラスの作成方法を制御することができます。クラス属性が定義される名前空間を管理することができます。

私たちの状況では、`Structure` サブクラスを定義するときにバリデータ型を使用できるようにするメタクラスを作成したいと思います。毎回これらのバリデータ型を明示的にインポートする必要はありません。

まず、`structure.py` ファイルを再度開きましょう。次のコマンドを使用して開くことができます。

```bash
code structure.py
```

ファイルが開いたら、`Structure` クラス定義の前にいくつかのコードを追加する必要があります。このコードは私たちのメタクラスを定義します。

```python
from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        """Prepare the namespace for the class being defined"""
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        """Create the new class using only the local namespace"""
        methods = methods.maps[0]  # Extract the local namespace
        return super().__new__(meta, name, bases, methods)
```

メタクラスを定義したので、`Structure` クラスを変更してこれを使用する必要があります。これにより、`Structure` を継承するすべてのクラスがメタクラスの機能を利用できるようになります。

```python
class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # Set the remaining keyword arguments
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Invalid argument: {name}')
            setattr(self, name, val)

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
```

このコードが何をするかを分解してみましょう。

1. `__prepare__()` メソッドは Python の特殊メソッドです。クラスが作成される前に呼び出されます。その役割は、クラス属性が定義される名前空間を準備することです。ここでは `ChainMap` を使用しています。`ChainMap` はレイヤード辞書を作成する便利なツールです。私たちの場合、バリデータ型を含め、クラス名前空間でアクセス可能にします。

2. `__new__()` メソッドは新しいクラスを作成する責任があります。ローカル名前空間のみを抽出します。これは `ChainMap` の最初の辞書です。バリデータ辞書は破棄します。なぜなら、すでに名前空間でバリデータ型を使用できるようにしているからです。

この設定により、`Structure` を継承するすべてのクラスは、バリデータ型を明示的にインポートする必要なく、すべてのバリデータ型にアクセスできます。

では、実装をテストしましょう。強化された `Structure` 基底クラスを使用して `Stock` クラスを作成します。

```bash
cat > stock.py << EOF
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
EOF
```

メタクラスが正しく機能している場合、バリデータ型をインポートせずに `Stock` クラスを定義できるはずです。これは、メタクラスがすでに名前空間でバリデータ型を使用できるようにしているからです。
