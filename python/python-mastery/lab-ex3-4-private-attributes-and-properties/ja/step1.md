# Private 属性の実装

Python では、属性がクラス内で内部的に使用されることを示すために、命名規則を使用します。これらの属性にはアンダースコア (`_`) をプレフィックスとして付けます。これは、これらの属性がパブリック API の一部ではなく、クラスの外部から直接アクセスすべきではないことを他の開発者に知らせるものです。

`stock.py` ファイルの現在の `Stock` クラスを見てみましょう。`types` という名前のクラス変数があります。

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

`types` クラス変数は、行データを変換するために内部的に使用されます。これが実装の詳細であることを示すために、private としてマークします。

**手順：**

1.  エディターで `stock.py` ファイルを開きます。

2.  `types` クラス変数を変更して、先頭にアンダースコアを追加し、`_types` に変更します。

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Rest of the class...
    ```

3.  `from_row` メソッドを更新して、名前を変更した変数 `_types` を使用します。

    ```python
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    ```

4.  `stock.py` ファイルを保存します。

5.  `test_stock.py` という名前の Python スクリプトを作成して、変更をテストします。次のコマンドを使用して、エディターでファイルを作成できます。

    ```bash
    touch /home/labex/project/test_stock.py
    ```

6.  次のコードを `test_stock.py` ファイルに追加します。このコードは、`Stock` クラスのインスタンスを作成し、それらに関する情報を出力します。

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
    print(f"Cost: {s.cost()}")

    # Create from row
    row = ['AAPL', '50', '142.5']
    apple = Stock.from_row(row)
    print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
    print(f"Cost: {apple.cost()}")
    ```

7.  ターミナルで次のコマンドを使用して、テストスクリプトを実行します。

    ```bash
    python /home/labex/project/test_stock.py
    ```

    次のような出力が表示されるはずです。

    ```
    Name: GOOG, Shares: 100, Price: 490.1
    Cost: 49010.0
    Name: AAPL, Shares: 50, Price: 142.5
    Cost: 7125.0
    ```
