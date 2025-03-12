# 検証用のクラスデコレータの作成

前のステップでは、実装は機能しましたが、冗長性がありました。`_fields` タプルとディスクリプタ属性の両方を指定する必要がありました。これはあまり効率的ではなく、改善することができます。Python では、クラスデコレータはこのプロセスを簡素化するのに役立つ強力なツールです。クラスデコレータは、クラスを引数として受け取り、何らかの方法でそれを変更し、変更されたクラスを返す関数です。クラスデコレータを使用することで、ディスクリプタからフィールド情報を自動的に抽出することができ、コードをよりクリーンで保守しやすくすることができます。

では、コードを簡素化するためのクラスデコレータを作成しましょう。以下は、従う必要がある手順です。

1. まず、`structure.py` ファイルを開きます。ターミナルで以下のコマンドを使用することができます。

```bash
code ~/project/structure.py
```

このコマンドは、コードエディタで `structure.py` ファイルを開きます。

2. 次に、`structure.py` ファイルの先頭、すべてのインポート文の直後に以下のコードを追加します。このコードは、私たちのクラスデコレータを定義します。

```python
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

このデコレータが何をするかを分解してみましょう。

- まず、`validators` という空のリストを作成します。次に、`vars(cls).items()` を使用してクラスのすべての属性を反復処理します。属性が `Validator` クラスのインスタンスである場合、その属性を `validators` リストに追加します。
- その後、クラスの `_fields` 属性を設定します。`validators` リスト内のバリデータから名前のリストを作成し、それを `cls._fields` に割り当てます。
- 最後に、クラスの `create_init()` メソッドを呼び出して `__init__` メソッドを生成し、変更されたクラスを返します。

3. コードを追加したら、`structure.py` ファイルを保存します。ファイルを保存することで、変更が保存されます。

4. 次に、この新しいデコレータを使用するように `stock.py` ファイルを変更する必要があります。以下のコマンドを使用して `stock.py` ファイルを開きます。

```bash
code ~/project/stock.py
```

5. `stock.py` ファイルを更新して、`validate_attributes` デコレータを使用するようにします。既存のコードを以下のコードに置き換えます。

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
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

行った変更に注目してください。

- `Stock` クラス定義のすぐ上に `@validate_attributes` デコレータを追加しました。これは、Python に `validate_attributes` デコレータを `Stock` クラスに適用するよう指示します。
- 明示的な `_fields` 宣言を削除しました。なぜなら、デコレータが自動的にそれを処理するからです。
- `Stock.create_init()` の呼び出しも削除しました。なぜなら、デコレータが `__init__` メソッドの作成を担当するからです。

結果として、クラスは今やよりシンプルでクリーンになりました。デコレータが、以前は手動で処理していたすべての詳細を担当します。

6. これらの変更を行った後、すべてが期待通りに動作することを検証する必要があります。以下のコマンドを使用して再度テストを実行します。

```bash
cd ~/project
python3 teststock.py
```

すべてが正しく動作していれば、次のような出力が表示されるはずです。

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

この出力は、すべてのテストが正常に合格したことを示しています。

また、対話的に `Stock` クラスをテストしてみましょう。ターミナルで以下のコマンドを実行します。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

次のような出力が表示されるはずです。

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

素晴らしい！フィールド宣言と初期化を自動的に処理することでコードを簡素化するクラスデコレータを正常に実装しました。これにより、コードがより効率的で保守しやすくなります。
