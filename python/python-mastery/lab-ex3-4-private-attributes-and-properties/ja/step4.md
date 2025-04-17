# メモリ最適化のための `__slots__` の使用

`__slots__` 属性は、クラスが持つことができる属性を制限します。インスタンスへの新しい属性の追加を防ぎ、メモリ使用量を削減します。

`Stock` クラスでは、`__slots__` を使用して以下を行います。

1.  属性の作成を、定義した属性のみに制限します。
2.  特に多数のインスタンスを作成する場合に、メモリ効率を向上させます。

**手順：**

1.  エディターで `stock.py` ファイルを開きます。
2.  `__slots__` クラス変数（class variable）を追加し、クラスで使用されるすべての private 属性名をリストします。

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Define slots to restrict attribute creation
        __slots__ = ('name', '_shares', '_price')

        # Rest of the class...
    ```

3.  ファイルを保存します。

4.  `test_slots.py` という名前のテストスクリプトを作成します。

    ```bash
    touch /home/labex/project/test_slots.py
    ```

5.  次のコードを `test_slots.py` ファイルに追加します。

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access existing attributes
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")

    # Try to add a new attribute
    try:
        s.extra = "This will fail"
        print(f"Extra: {s.extra}")
    except AttributeError as e:
        print(f"Error: {e}")
    ```

6.  テストスクリプトを実行します。

    ```bash
    python /home/labex/project/test_slots.py
    ```

    定義された属性にアクセスできるものの、新しい属性を追加しようとすると `AttributeError` が発生することが出力に表示されるはずです。

    ```plaintext
    Name: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    Error: 'Stock' object has no attribute 'extra'
    ```
