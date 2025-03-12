# メソッドをプロパティに変換する

Pythonでは、プロパティは強力な機能であり、属性にアクセスするのと同じような方法で計算値にアクセスすることができます。通常、メソッドから値を取得する場合、そのメソッドを呼び出すために括弧を使用する必要があります。しかし、プロパティを使用すると、これらの括弧が不要になり、コードがよりクリーンになり、通常の属性にアクセスする方法と整合性が取れます。

現在の `Stock` クラスを見てみましょう。このクラスには、株式の総コストを計算する `cost()` メソッドがあります。このメソッドは、株式数に1株あたりの価格を掛けることで総コストを求めます。`cost()` メソッドは次のようになっています。

```python
def cost(self):
    return self.shares * self.price
```

このメソッドを使用してコストの値を取得するには、括弧を付けて呼び出す必要があります。

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

しかし、コードを改善することができます。`cost()` メソッドをプロパティに変換することで、括弧を使用せずに他の属性にアクセスするのと同じようにコストの値にアクセスすることができます。次のようになります。

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

## 手順:

1. まず、エディタで `stock.py` ファイルを開く必要があります。このファイルに `Stock` クラスが定義されており、ここで変更を加えます。ターミナルで次のコマンドを使用します。

   ```bash
   code /home/labex/project/stock.py
   ```

2. `stock.py` ファイル内で、`cost()` メソッドをプロパティに置き換えます。これには `@property` デコレータを使用します。`@property` デコレータは、次のメソッドをプロパティとして扱うようPythonに指示します。`cost()` メソッドを次のコードに置き換えます。

   ```python
   @property
   def cost(self):
       return self.shares * self.price
   ```

3. 変更を加えた後、`stock.py` ファイルを保存します。これにより、変更が保存され、後で使用できるようになります。

4. 次に、新しいプロパティをテストするための簡単なPythonスクリプトを作成する必要があります。次のコマンドを使用してエディタで `test_property.py` という名前の新しいファイルを開きます。

   ```bash
   code /home/labex/project/test_property.py
   ```

5. `test_property.py` ファイルに、`Stock` インスタンスを作成して `cost` プロパティにアクセスするコードを追加します。次のコードを追加してください。

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

6. 最後に、テストスクリプトを実行して、プロパティが期待通りに動作するか確認します。ターミナルで次のコマンドを使用します。
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

`cost` を属性として（括弧なしで）アクセスできるようになったことに注目してください。これにより、`name`、`shares`、`price` などの他の属性にアクセスする方法とコードが整合性を持ち、読みやすく保守しやすくなります。
