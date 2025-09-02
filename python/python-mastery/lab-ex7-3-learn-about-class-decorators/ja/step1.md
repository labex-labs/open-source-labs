# ディスクリプタによる型チェックの実装

このステップでは、型チェックにディスクリプタを使用する `Stock` クラスを作成します。しかし、まずディスクリプタとは何かを理解しましょう。ディスクリプタは Python の非常に強力な機能です。これにより、クラスの属性へのアクセス方法を制御できます。

ディスクリプタは、他のオブジェクトの属性へのアクセス方法を定義するオブジェクトです。これは、`__get__`、`__set__`、`__delete__` のような特殊なメソッドを実装することによって行われます。これらのメソッドにより、ディスクリプタは属性の取得、設定、削除の方法を管理できます。ディスクリプタは、検証、型チェック、計算プロパティの実装に非常に役立ちます。例えば、ディスクリプタを使用して、属性が常に正の数または特定の形式の文字列であることを保証できます。

`validate.py` ファイルには、すでにバリデータクラス (`String`、`PositiveInteger`、`PositiveFloat`) が含まれています。これらのクラスを使用して、`Stock` クラスの属性を検証できます。

それでは、ディスクリプタを使用した `Stock` クラスを作成しましょう。

1. まず、エディタで `stock.py` ファイルを開きます。

2. ファイルが開いたら、プレースホルダーの内容を次のコードに置き換えます。

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# _fields に基づいて __init__ メソッドを作成します
Stock.create_init()
```

このコードが何をするのかを分解してみましょう。`_fields` タプルは `Stock` クラスの属性を定義します。これらは、`Stock` オブジェクトが持つ属性の名前です。

`name`、`shares`、`price` 属性はディスクリプタオブジェクトとして定義されています。`String()` ディスクリプタは、`name` 属性が文字列であることを保証します。`PositiveInteger()` ディスクリプタは、`shares` 属性が正の整数であることを保証します。そして `PositiveFloat()` ディスクリプタは、`price` 属性が正の浮動小数点数であることを保証します。

`cost` プロパティは計算プロパティです。これは、株式数と 1 株あたりの価格に基づいて株式の総コストを計算します。

`sell` メソッドは、株式数を減らすために使用されます。売却する株式数を指定してこのメソッドを呼び出すと、その数が `shares` 属性から差し引かれます。

`Stock.create_init()` 行は、クラスの `__init__` メソッドを動的に作成します。このメソッドにより、`name`、`shares`、`price` 属性の値を渡して `Stock` オブジェクトを作成できます。

3. コードを追加したら、ファイルを保存します。これにより、変更が保存され、テストを実行する際に使用できるようになります。

4. それでは、テストを実行して実装を確認しましょう。まず、次のコマンドを実行してディレクトリを `~/project` ディレクトリに変更します。

```bash
cd ~/project
```

次に、次のコマンドを使用してテストを実行します。

```bash
python3 teststock.py
```

実装が正しければ、次のような出力が表示されるはずです。

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

この出力は、すべてのテストが合格したことを意味します。ディスクリプタは、各属性の型を正常に検証しています！

Python インタープリタで `Stock` オブジェクトを作成してみましょう。まず、`~/project` ディレクトリにいることを確認してください。次に、次のコマンドを実行します。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

次の出力が表示されるはずです。

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

型チェックのためのディスクリプタを正常に実装しました！それでは、このコードをさらに改善しましょう。
