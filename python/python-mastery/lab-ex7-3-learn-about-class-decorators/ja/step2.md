# 検証のためのクラスデコレータの作成

前のステップでは、実装は機能しましたが、冗長性がありました。`_fields` タプルとディスクリプタ属性の両方を指定する必要がありました。これはあまり効率的ではなく、改善できます。Python では、クラスデコレータは、このプロセスを簡素化するのに役立つ強力なツールです。クラスデコレータは、クラスを引数として受け取り、それを何らかの方法で変更してから、変更されたクラスを返す関数です。クラスデコレータを使用することで、ディスクリプタからフィールド情報を自動的に抽出でき、コードがよりクリーンで保守しやすくなります。

コードを簡素化するためにクラスデコレータを作成しましょう。以下に、従う必要がある手順を示します。

1. まず、エディタで `structure.py` ファイルを開きます。

2. 次に、`structure.py` ファイルの先頭、インポート文の直後に次のコードを追加します。このコードはクラスデコレータを定義します。

```python
from validate import Validator

def validate_attributes(cls):
    """
    Validator インスタンスを抽出し、_fields リストを自動的に構築する
    クラスデコレータ
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # バリデータ名に基づいて _fields を設定します
    cls._fields = [val.name for val in validators]

    # 初期化メソッドを作成します
    cls.create_init()

    return cls
```

このデコレータが何をするのかを分解してみましょう。

- まず、`validators` という空のリストを作成します。次に、`vars(cls).items()` を使用してクラスのすべての属性を反復処理します。属性が `Validator` クラスのインスタンスである場合、その属性を `validators` リストに追加します。
- その後、クラスの `_fields` 属性を設定します。`validators` リスト内のバリデータから名前のリストを作成し、それを `cls._fields` に割り当てます。
- 最後に、クラスの `create_init()` メソッドを呼び出して `__init__` メソッドを生成し、変更されたクラスを返します。

3. コードを追加したら、`structure.py` ファイルを保存します。ファイルを保存することで、変更が保持されます。

4. 次に、この新しいデコレータを使用するように `stock.py` ファイルを変更する必要があります。エディタで `stock.py` ファイルを開きます。

5. `validate_attributes` デコレータを使用するように `stock.py` ファイルを更新します。既存のコードを次のコードに置き換えます。

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

変更点に注目してください。

- `Stock` クラス定義のすぐ上に `@validate_attributes` デコレータを追加しました。これにより、Python は `validate_attributes` デコレータを `Stock` クラスに適用するように指示されます。
- デコレータが自動的に処理するため、明示的な `_fields` 宣言を削除しました。
- デコレータが `__init__` メソッドの作成を担当するため、`Stock.create_init()` の呼び出しも削除しました。

その結果、クラスはよりシンプルでクリーンになりました。デコレータは、以前は手動で処理していたすべての詳細を処理します。

6. これらの変更を行った後、すべてが期待どおりに機能することを確認する必要があります。次のコマンドを使用して、再度テストを実行します。

```bash
cd ~/project
python3 teststock.py
```

すべてが正しく機能していれば、次の出力が表示されるはずです。

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

この出力は、すべてのテストが正常に合格したことを示しています。

`Stock` クラスをインタラクティブにテストしましょう。ターミナルで次のコマンドを実行します。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

次の出力が表示されるはずです。

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

素晴らしい！フィールド宣言と初期化を自動的に処理することでコードを簡素化するクラスデコレータを正常に実装しました。これにより、コードはより効率的で保守しやすくなります。
