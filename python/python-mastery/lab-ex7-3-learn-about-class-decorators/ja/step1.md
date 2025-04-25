# ディスクリプタを使った型チェックの実装

このステップでは、型チェックにディスクリプタを使用する `Stock` クラスを作成します。まずは、ディスクリプタが何であるかを理解しましょう。ディスクリプタは Python の非常に強力な機能です。クラス内の属性へのアクセス方法を制御することができます。

ディスクリプタは、他のオブジェクトの属性へのアクセス方法を定義するオブジェクトです。これは、`__get__`、`__set__`、`__delete__` などの特殊メソッドを実装することで行われます。これらのメソッドにより、ディスクリプタは属性の取得、設定、削除方法を管理することができます。ディスクリプタは、検証、型チェック、および計算属性の実装に非常に役立ちます。たとえば、属性が常に正の数または特定の形式の文字列であることを確認するためにディスクリプタを使用することができます。

`validate.py` ファイルには、すでにバリデータクラス (`String`、`PositiveInteger`、`PositiveFloat`) があります。これらのクラスを使用して、`Stock` クラスの属性を検証することができます。

では、ディスクリプタを使用した `Stock` クラスを作成しましょう。

1. まず、エディタで `stock.py` ファイルを開きます。ターミナルで以下のコマンドを実行することでこれを行うことができます。

```bash
code ~/project/stock.py
```

このコマンドは、`code` エディタを使用して、`~/project` ディレクトリにある `stock.py` ファイルを開きます。

2. ファイルが開いたら、プレースホルダーの内容を以下のコードに置き換えます。

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

# Create an __init__ method based on _fields
Stock.create_init()
```

このコードが何をするかを分解してみましょう。`_fields` タプルは、`Stock` クラスの属性を定義します。これらは、`Stock` オブジェクトが持つ属性の名前です。

`name`、`shares`、`price` 属性は、ディスクリプタオブジェクトとして定義されています。`String()` ディスクリプタは、`name` 属性が文字列であることを保証します。`PositiveInteger()` ディスクリプタは、`shares` 属性が正の整数であることを確認します。そして、`PositiveFloat()` ディスクリプタは、`price` 属性が正の浮動小数点数であることを保証します。

`cost` プロパティは計算属性です。株式の総コストを、株式数と 1 株あたりの価格に基づいて計算します。

`sell` メソッドは、株式数を減らすために使用されます。このメソッドを売却する株式数とともに呼び出すと、`shares` 属性からその数が減算されます。

`Stock.create_init()` 行は、クラスに動的に `__init__` メソッドを作成します。このメソッドにより、`name`、`shares`、`price` 属性の値を渡して `Stock` オブジェクトを作成することができます。

3. コードを追加したら、ファイルを保存します。これにより、変更が保存され、テストを実行するときに使用できるようになります。

4. では、実装を検証するためにテストを実行しましょう。まず、以下のコマンドを実行して、`~/project` ディレクトリに移動します。

```bash
cd ~/project
```

次に、以下のコマンドを使用してテストを実行します。

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

この出力は、すべてのテストが合格したことを意味します。ディスクリプタが各属性の型を正常に検証しています！

Python インタープリターで `Stock` オブジェクトを作成してみましょう。まず、`~/project` ディレクトリにいることを確認してください。次に、以下のコマンドを実行します。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

次のような出力が表示されるはずです。

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

型チェック用のディスクリプタを正常に実装しました！では、このコードをさらに改善しましょう。
