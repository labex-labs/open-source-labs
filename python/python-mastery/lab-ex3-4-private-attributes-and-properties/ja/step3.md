# プロパティの検証の実装

プロパティを使用すると、属性値の取得、設定、および削除の方法を制御することもできます。これは、属性に検証を追加し、値が特定の基準を満たしていることを確認するのに役立ちます。

`Stock` クラスでは、`shares` が負でない整数であり、`price` が負でない浮動小数点数であることを確認する必要があります。これを実現するために、getter（ゲッター）と setter（セッター）とともにプロパティデコレーターを使用します。

**手順：**

1.  エディターで `stock.py` ファイルを開きます。

2.  private 属性 `_shares` と `_price` を `Stock` クラスに追加し、コンストラクター（constructor）を変更してそれらを使用します。

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares  # Using private attribute
        self._price = price    # Using private attribute
    ```

3.  検証を使用して `shares` と `price` のプロパティを定義します。

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected integer")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Expected float")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

4.  コンストラクターを更新して、検証のためにプロパティセッターを使用します。

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares  # Using property setter
        self.price = price    # Using property setter
    ```

5.  `stock.py` ファイルを保存します。

6.  `test_validation.py` という名前のテストスクリプトを作成します。

    ```bash
    touch /home/labex/project/test_validation.py
    ```

7.  次のコードを `test_validation.py` ファイルに追加します。

    ```python
    from stock import Stock

    # Create a valid stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

    # Test valid updates
    try:
        s.shares = 50  # Valid update
        print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting shares=50: {e}")

    try:
        s.price = 123.45  # Valid update
        print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting price=123.45: {e}")

    # Test invalid updates
    try:
        s.shares = "50"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares='50': {e}")

    try:
        s.shares = -10  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares=-10: {e}")

    try:
        s.price = "123.45"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price='123.45': {e}")

    try:
        s.price = -10.0  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price=-10.0: {e}")
    ```

8.  テストスクリプトを実行します。

    ```bash
    python /home/labex/project/test_validation.py
    ```

    有効な更新が成功し、無効な更新に対して適切なエラーメッセージが表示される出力が表示されるはずです。

    ```plaintext
    Initial: Name=GOOG, Shares=100, Price=490.1, Cost=49010.0
    After setting shares=50: Shares=50, Cost=24505.0
    After setting price=123.45: Price=123.45, Cost=6172.5
    Error setting shares='50': Expected integer
    Error setting shares=-10: shares must be >= 0
    Error setting price='123.45': Expected float
    Error setting price=-10.0: price must be >= 0
    ```
