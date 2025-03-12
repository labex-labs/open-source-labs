# 検証器を株式クラスに適用する

このステップでは、実際のシチュエーションで検証器がどのように機能するかを見ていきます。検証器は、使用するデータが特定のルールを満たしていることを確認する小さなチェッカーのようなものです。`Stock`クラスを作成します。クラスはオブジェクトを作成するための青写真のようなものです。この場合、`Stock`クラスは株式市場の株を表し、検証器を使ってその属性の値（株数や価格など）が有効であることを確認します。

## 株式クラスの作成

まず、新しいファイルを作成する必要があります。WebIDEで`stock.py`という名前の新しいファイルを作成します。このファイルには`Stock`クラスのコードが記述されます。では、`stock.py`ファイルに以下のコードを追加しましょう。

```python
# stock.py
from validate import PositiveInteger, PositiveFloat

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    def cost(self):
        return self.shares * self.price
```

このコードが何をするかを分解して説明しましょう。

1. `validate`モジュールから`PositiveInteger`と`PositiveFloat`の検証器をインポートします。これらの検証器は、株数が正の整数で、価格が正の浮動小数点数であることを確認するのに役立ちます。
2. 次に`Stock`クラスを定義します。クラスの中には`__init__`メソッドがあります。このメソッドは、新しい`Stock`オブジェクトを作成するときに呼び出されます。`name`、`shares`、`price`の3つのパラメータを受け取り、それらをオブジェクトの属性に割り当てます。
3. プロパティとセッターを使って、`shares`と`price`の値を検証します。プロパティは属性へのアクセスを制御する方法であり、セッターはその属性の値を設定しようとするときに呼び出されるメソッドです。`shares`属性を設定するとき、`PositiveInteger.check`メソッドが呼び出されて、値が正の整数であることが確認されます。同様に、`price`属性を設定するとき、`PositiveFloat.check`メソッドが呼び出されて、値が正の浮動小数点数であることが確認されます。
4. 最後に、`cost`メソッドがあります。このメソッドは、株数に価格を掛けることで株の総コストを計算します。

## 株式クラスのテスト

`Stock`クラスを作成したので、検証器が正しく機能しているかをテストする必要があります。新しいターミナルを開き、Pythonインタープリタを起動します。以下のコマンドを実行することで行えます。

```bash
python3
```

Pythonインタープリタが起動したら、`Stock`クラスをインポートしてテストすることができます。Pythonインタープリタに以下のコードを入力します。

```python
from stock import Stock

# Create a valid stock
s = Stock('GOOG', 100, 490.10)
print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try setting an invalid shares value
try:
    s.shares = -10
except ValueError as e:
    print(f"Error setting shares: {e}")

# Try setting an invalid price value
try:
    s.price = "not a price"
except TypeError as e:
    print(f"Error setting price: {e}")
```

このコードを実行すると、以下のような出力が表示されるはずです。

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Error setting shares: Expected >= 0
Error setting price: Expected <class 'float'>
```

この出力は、検証器が期待通りに機能していることを示しています。`Stock`クラスは、`shares`と`price`に無効な値を設定することを許可しません。無効な値を設定しようとすると、エラーが発生し、そのエラーをキャッチして表示することができます。

## 継承の役割の理解

検証器を使用する大きな利点の1つは、異なる検証ルールを簡単に組み合わせることができることです。継承はPythonにおける強力な概念で、既存のクラスを基に新しいクラスを作成することができます。多重継承を使うと、`super()`関数を使って複数の親クラスのメソッドを呼び出すことができます。

たとえば、株式の名前が空でないことを確認したい場合は、以下の手順に従うことができます。

1. `validate`モジュールから`NonEmptyString`検証器をインポートします。この検証器は、株式の名前が空文字列でないことを確認するのに役立ちます。
2. `Stock`クラスに`name`属性のプロパティセッターを追加します。このセッターは、`NonEmptyString.check()`メソッドを使って株式の名前を検証します。

これは、継承、特に`super()`関数を使った多重継承が、柔軟でさまざまな組み合わせで再利用できるコンポーネントを構築することを可能にすることを示しています。

テストが終了したら、以下のコマンドを実行してPythonインタープリタを終了することができます。

```python
exit()
```
