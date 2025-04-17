# クラス変数との型検証の調整

現在、`Stock` クラスは、型処理のために `_types` クラス変数とプロパティセッターの両方を使用しています。一貫性と保守性を向上させるために、これらのメカニズムを調整して、同じ型情報を使用するようにします。

**手順：**

1.  エディターで `stock.py` ファイルを開きます。

2.  `_types` クラス変数で定義された型を使用するようにプロパティセッターを変更します。

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1].__name__}")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2].__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

3.  `stock.py` ファイルを保存します。

4.  `test_subclass.py` という名前のテストスクリプトを作成します。

    ```bash
    touch /home/labex/project/test_subclass.py
    ```

5.  次のコードを `test_subclass.py` ファイルに追加します。

    ```python
    from stock import Stock
    from decimal import Decimal

    # Create a subclass with different types
    class DStock(Stock):
        _types = (str, int, Decimal)

    # Test the base class
    s = Stock('GOOG', 100, 490.10)
    print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

    # Test valid update with float
    try:
        s.price = 500.25
        print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
    except Exception as e:
        print(f"Error updating Stock price: {e}")

    # Test the subclass with Decimal
    ds = DStock('AAPL', 50, Decimal('142.50'))
    print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

    # Test invalid update with float (should require Decimal)
    try:
        ds.price = 150.75
        print(f"Updated DStock price: {ds.price}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")

    # Test valid update with Decimal
    try:
        ds.price = Decimal('155.25')
        print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")
    ```

6.  テストスクリプトを実行します。

    ```bash
    python /home/labex/project/test_subclass.py
    ```

    基本の `Stock` クラスは price（価格）に float（浮動小数点数）値を受け入れますが、`DStock` サブクラスは `Decimal` 値を必要とすることがわかります。

    ```plaintext
    Stock: GOOG, Shares: 100, Price: 490.1, Cost: 49010.0
    Updated Stock price: 500.25, Cost: 50025.0
    DStock: AAPL, Shares: 50, Price: 142.50, Cost: 7125.00
    Error updating DStock price: Expected Decimal
    Updated DStock price: 155.25, Cost: 7762.50
    ```
