# メソッドをプロパティに変換する

Python のプロパティを使用すると、計算された値を属性のようにアクセスできます。これにより、メソッドを呼び出すときに括弧が不要になり、コードがよりクリーンで一貫性のあるものになります。

現在、`Stock` クラスには、株式の総コストを計算する `cost()` メソッドがあります。

```python
def cost(self):
    return self.shares * self.price
```

コスト値を取得するには、括弧を付けて呼び出す必要があります。

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

`cost()` メソッドをプロパティに変換することで、これを改善し、括弧なしでコスト値にアクセスできるようにすることができます。

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

**手順：**

1.  エディターで `stock.py` ファイルを開きます。

2.  `@property` デコレーターを使用して、`cost()` メソッドをプロパティに置き換えます。

    ```python
    @property
    def cost(self):
        return self.shares * self.price
    ```

3.  `stock.py` ファイルを保存します。

4.  エディターで `test_property.py` という名前の新しいファイルを作成します。

    ```bash
    touch /home/labex/project/test_property.py
    ```

5.  次のコードを `test_property.py` ファイルに追加して、`Stock` インスタンスを作成し、`cost` プロパティにアクセスします。

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access cost as a property (no parentheses)
    print(f"Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")  # Using the property
    ```

6.  テストスクリプトを実行します。

    ```bash
    python /home/labex/project/test_property.py
    ```

    次のような出力が表示されるはずです。

    ```
    Stock: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    ```
