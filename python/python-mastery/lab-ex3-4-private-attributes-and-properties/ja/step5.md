# クラス変数と型バリデーションの調和

Python のプログラミングの旅で、`Stock` クラスを作成しました。このクラスは現在、データ型を扱う 2 つの異なる方法を持っています。これらのメカニズムを理解することは、コードをより良く管理し整理するのに役立つため、非常に重要です。

最初のメカニズムは `_types` クラス変数です。この変数は、行からのデータを変換するために使用されます。行形式のデータを取得したとき、`_types` 変数はそのデータを `Stock` クラスに適した型に変換するのに役立ちます。

2 番目のメカニズムはプロパティセッターです。これらのセッターは型チェックを強制します。`Stock` クラスのプロパティに値を設定しようとするたびに、プロパティセッターはその値が正しい型であることを確認します。

しかし、2 つの別々のメカニズムがあると、クラスのメンテナンスが困難になります。この問題を解決するために、これら 2 つのメカニズムを調和させて、同じ型情報を使用するようにする必要があります。これにより、クラスの一貫性が保たれ、サブクラスを作成する際により信頼性が高くなります。

## 手順：

1. まず、エディタで `stock.py` ファイルを開く必要があります。このファイルには `Stock` クラスのコードが含まれています。開くには、ターミナルで次のコマンドを実行します。

   ```bash
   code /home/labex/project/stock.py
   ```

2. 次に、`stock.py` ファイル内のプロパティセッターを変更します。`_types` クラス変数で定義された型を使用するようにします。これにより、プロパティセッターの型チェックが `_types` 変数による型変換と一致することが保証されます。プロパティセッターを次のように変更します。

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

3. これらの変更を加えた後、`stock.py` ファイルを保存します。ファイルを保存することで、変更が保存されます。

4. 次に、異なる型を持つサブクラス化が期待通りに動作することを確認するためのテストスクリプトを作成します。このスクリプトを作成するには、ターミナルで次のコマンドを実行します。

   ```bash
   code /home/labex/project/test_subclass.py
   ```

5. 次に、`test_subclass.py` ファイルに次のコードを追加します。このコードは、異なる型を持つ `Stock` クラスのサブクラスを作成し、基底クラスとサブクラスの両方をテストします。

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

6. 最後に、テストスクリプトを実行して結果を確認します。ターミナルで次のコマンドを実行します。

   ```bash
   python /home/labex/project/test_subclass.py
   ```

テストスクリプトを実行すると、基底の `Stock` クラスは価格に浮動小数点数値を受け入れるのに対し、`DStock` サブクラスは `Decimal` 値を必要とすることがわかるはずです。これは、型の調和が期待通りに機能したことを示しています。

### 考察

`Stock` クラスの型情報を調和させることで、クラスをより一貫性のあるものにしました。現在、プロパティセッターは `from_row` メソッドと同じ型情報を使用しています。この一貫性により、クラスのメンテナンスと拡張が容易になり、特にサブクラスを作成する際に便利です。

現在の `Stock` クラスの実装は、単純な概念に対して複雑に見えるかもしれませんが、カプセル化と型安全性の重要な Python テクニックを示しています。実際のアプリケーションでは、dataclasses やサードパーティライブラリなどのツールを使用して、このような実装を簡素化することができます。これらのツールにより、コードをより簡潔で管理しやすくすることができます。
