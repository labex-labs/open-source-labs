# Stock クラスの書き換え

よく定義された `Structure` 基底クラスができたので、`Stock` クラスを書き換えましょう。この基底クラスを使用することで、コードを簡素化し、より整理されたものにすることができます。`Structure` クラスは、`Stock` クラスで再利用できる一連の共通機能を提供します。これは、コードの保守性と読みやすさにとって大きな利点となります。

## 新しい Stock クラスの作成

まず、`stock.py` という名前の新しいファイルを作成しましょう。このファイルには、書き換えた `Stock` クラスが含まれます。`stock.py` ファイルに入れるコードは以下の通りです。

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        """
        Calculate the cost as shares * price
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        Sell a number of shares
        """
        self.shares -= nshares
```

この新しい `Stock` クラスが何をするかを分解してみましょう。

1. `Structure` クラスを継承しています。これは、`Stock` クラスが `Structure` クラスが提供するすべての機能を使用できることを意味します。利点の 1 つは、`Structure` クラスが属性の割り当てを自動的に処理するため、自分で `__init__` メソッドを書く必要がないことです。
2. `_fields` を定義しています。これは、`Stock` クラスの属性を指定するタプルです。これらの属性は `name`、`shares`、`price` です。
3. `cost` プロパティが定義されており、株式の総コストを計算します。`shares` の数に `price` を掛けた値を返します。
4. `sell` メソッドは、株式の数を減らすために使用されます。このメソッドを売却する株式の数で呼び出すと、現在の株式数からその数が減算されます。

## 新しい Stock クラスのテスト

新しい `Stock` クラスが期待通りに動作することを確認するために、テストファイルを作成する必要があります。以下のコードを含む `test_stock.py` という名前のファイルを作成しましょう。

```python
# test_stock.py
from stock import Stock

# Create a stock
s = Stock('GOOG', 100, 490.1)

# Check the attributes
print(f"Stock: {s}")
print(f"Name: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost}")

# Sell some shares
print("\nSelling 20 shares...")
s.sell(20)
print(f"Shares after selling: {s.shares}")
print(f"Cost after selling: {s.cost}")

# Try to set an invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.prices = 500  # Invalid attribute (should be 'price')
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

このテストファイルでは、まず `stock.py` ファイルから `Stock` クラスをインポートします。次に、名前が 'GOOG'、株式数が 100、価格が 490.1 の `Stock` クラスのインスタンスを作成します。株式の属性を出力して、正しく設定されているかを確認します。その後、20 株を売却し、新しい株式数と新しいコストを出力します。最後に、無効な属性 `prices`（正しくは `price` であるべき）を設定しようとします。`Stock` クラスが正しく動作していれば、`AttributeError` が発生するはずです。

テストを実行するには、ターミナルを開き、以下のコマンドを入力します。

```bash
python3 test_stock.py
```

期待される出力は以下の通りです。

```
Stock: Stock('GOOG', 100, 490.1)
Name: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0

Selling 20 shares...
Shares after selling: 80
Cost after selling: 39208.0

Trying to set an invalid attribute:
Error correctly caught: No attribute prices
```

## ユニットテストの実行

前の演習でユニットテストを作成している場合は、新しい実装に対してそれらを実行することができます。ターミナルで以下のコマンドを入力します。

```bash
python3 teststock.py
```

一部のテストが失敗する場合があります。これは、まだ実装していない特定の動作やメソッドを期待しているためかもしれません。心配しないでください！将来の演習でこの基礎を元にさらに構築していきます。

## 進捗の振り返り

ここまでで達成したことを振り返ってみましょう。

1. 再利用可能な `Structure` 基底クラスを作成しました。このクラスは以下のことを行います。

   - 属性の割り当てを自動的に処理するため、多くの繰り返しコードを書く必要がなくなります。
   - 良い文字列表現を提供するため、オブジェクトの印刷とデバッグが容易になります。
   - 属性名を制限してエラーを防止するため、コードがより堅牢になります。

2. `Stock` クラスを書き換えました。このクラスは以下のことを行います。
   - `Structure` クラスを継承して共通機能を再利用します。
   - フィールドとドメイン固有のメソッドのみを定義するため、クラスが焦点を絞り、クリーンになります。
   - 明確でシンプルな設計なので、理解と保守が容易です。

このアプローチは、コードにいくつかの利点をもたらします。

- 繰り返しが少ないため、保守性が向上します。共通機能に何かを変更する必要がある場合、`Structure` クラスでのみ変更すればよいからです。
- `Structure` クラスによるより良いエラーチェックのため、堅牢性が向上します。
- 各クラスの責任が明確なため、読みやすさが向上します。

将来の演習では、この基礎を元にさらに洗練された株式ポートフォリオ管理システムを作成していきます。
