# クラス変数と継承

このステップでは、クラス変数が継承とどのように相互作用し、カスタマイズのメカニズムとしてどのように機能するかを探っていきます。Python では、継承によりサブクラスは基底クラスから属性とメソッドを継承することができます。クラス変数は、クラス自体に属する変数であり、クラスの特定のインスタンスに属するものではありません。これらがどのように連携するかを理解することは、柔軟で保守可能なコードを作成するために重要です。

## 継承におけるクラス変数

サブクラスが基底クラスから継承すると、自動的に基底クラスのクラス変数にアクセスできるようになります。ただし、サブクラスはこれらのクラス変数を上書きすることができます。こうすることで、サブクラスは基底クラスに影響を与えることなく自身の振る舞いを変更することができます。これは非常に強力な機能であり、特定のニーズに合わせてサブクラスの振る舞いをカスタマイズすることができます。

## 特殊な Stock クラスの作成

`Stock` クラスのサブクラスを作成しましょう。これを `DStock` と呼び、これは Decimal Stock の略です。`DStock` と通常の `Stock` クラスの主な違いは、`DStock` が価格の値に `float` ではなく `Decimal` 型を使用することです。金融計算では精度が非常に重要であり、`Decimal` 型は `float` と比較してより正確な 10 進数演算を提供します。

このサブクラスを作成するには、`decimal_stock.py` という名前の新しいファイルを作成します。このファイルに入れる必要があるコードは次のとおりです。

```python
# decimal_stock.py
from decimal import Decimal
from stock import Stock

class DStock(Stock):
    """
    A specialized version of Stock that uses Decimal for prices
    """
    types = (str, int, Decimal)  # Override the types class variable

# Test the subclass
if __name__ == "__main__":
    # Create a DStock from row data
    row = ['AA', '100', '32.20']
    ds = DStock.from_row(row)

    print(f"DStock: {ds.name}")
    print(f"Shares: {ds.shares}")
    print(f"Price: {ds.price} (type: {type(ds.price).__name__})")
    print(f"Cost: {ds.cost()} (type: {type(ds.cost()).__name__})")

    # For comparison, create a regular Stock from the same data
    s = Stock.from_row(row)
    print(f"\nRegular Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price} (type: {type(s.price).__name__})")
    print(f"Cost: {s.cost()} (type: {type(s.cost()).__name__})")
```

上記のコードで `decimal_stock.py` ファイルを作成したら、結果を確認するために実行する必要があります。ターミナルを開き、以下の手順に従います。

```bash
cd ~/project
python decimal_stock.py
```

以下のような出力が表示されるはずです。

```
DStock: AA
Shares: 100
Price: 32.20 (type: Decimal)
Cost: 3220.0 (type: Decimal)

Regular Stock: AA
Shares: 100
Price: 32.2 (type: float)
Cost: 3220.0 (type: float)
```

## クラス変数と継承に関する要点

この例から、いくつかの重要な結論を導き出すことができます。

1. `DStock` クラスは、`cost()` メソッドなど、`Stock` クラスのすべてのメソッドを再定義することなく継承します。これは継承の主な利点の 1 つであり、冗長なコードを書く手間を省いてくれます。
2. `types` クラス変数を単に上書きすることで、`DStock` の新しいインスタンスを作成する際のデータの変換方法を変更しました。これは、クラス変数がサブクラスの振る舞いをカスタマイズするためにどのように使用できるかを示しています。
3. 基底クラスである `Stock` は変更されず、依然として `float` 値で動作します。これは、サブクラスに対して行った変更が基底クラスに影響を与えないことを意味しており、良い設計原則です。
4. `from_row()` クラスメソッドは、`Stock` クラスと `DStock` クラスの両方で正しく動作します。これは、同じメソッドが異なるサブクラスで使用できることを示しており、継承の強力さを実証しています。

この例は、クラス変数が構成メカニズムとしてどのように使用できるかを明確に示しています。サブクラスはこれらの変数を上書きして、メソッドを書き直すことなく自身の振る舞いをカスタマイズすることができます。

## 設計に関する議論

型変換を `__init__` メソッドに配置する別のアプローチを考えてみましょう。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

このアプローチでは、次のようにデータの行から `Stock` オブジェクトを作成することができます。

```python
row = ['AA', '100', '32.20']
s = Stock(*row)
```

このアプローチは一見すると簡単に見えるかもしれませんが、いくつかの欠点があります。

1. オブジェクトの初期化とデータの変換という 2 つの異なる関心事を混在させています。これにより、コードが理解しにくく、保守も難しくなります。
2. `__init__` メソッドは、入力がすでに正しい型である場合でも常に変換を行うため、柔軟性が低下します。
3. サブクラスが変換プロセスをカスタマイズする方法が制限されます。変換ロジックが `__init__` メソッドに組み込まれている場合、サブクラスが変換ロジックを変更するのは難しくなります。
4. コードが脆弱になります。変換のいずれかが失敗すると、オブジェクトを作成できず、プログラムにエラーが発生する可能性があります。

一方、クラスメソッドのアプローチはこれらの関心事を分離します。これにより、コードの各部分が単一の責任を持つため、コードがより保守可能で柔軟になります。
