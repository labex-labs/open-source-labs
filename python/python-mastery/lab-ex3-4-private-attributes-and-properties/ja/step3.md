# プロパティのバリデーションの実装

Pythonのプロパティは強力な機能です。これらは、計算値を通常の属性のようにアクセスできるだけでなく、属性値の取得、設定、削除方法を制御することができます。この制御は、属性にバリデーションを追加する必要がある場合に非常に有用です。バリデーションにより、属性に割り当てられる値が特定の基準を満たすことが保証され、データの整合性が維持されます。

`Stock` クラスには、`shares` と `price` という2つの重要な属性があります。`shares` が非負の整数で、`price` が非負の浮動小数点数であることを確認したいと思います。このバリデーションを実現するために、プロパティデコレータとゲッター、セッターを使用します。

## 手順:

1. まず、エディタで `stock.py` ファイルを開く必要があります。ここで `Stock` クラスにすべての変更を加えます。ターミナルで次のコマンドを使用します。

   ```bash
   code /home/labex/project/stock.py
   ```

2. Pythonでは、クラス変数の実際の値を格納するためにプライベート属性を使用できます。プライベート属性は先頭にアンダースコアが付きます。`Stock` クラスにプライベート属性 `_shares` と `_price` を追加し、コンストラクタを変更してこれらを使用するようにします。コンストラクタは、クラスの新しいインスタンスを作成するときに呼び出されるメソッドです。次のように行います。

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self._shares = shares  # Using private attribute
       self._price = price    # Using private attribute
   ```

3. 次に、適切なバリデーションを持つ `shares` と `price` のプロパティを定義します。プロパティは、ゲッターメソッドに `@property` デコレータを、セッターメソッドに `@<property_name>.setter` デコレータを使用して定義されます。ゲッターメソッドは属性の値を取得するために使用され、セッターメソッドは値を設定するために使用されます。バリデーション付きのプロパティ定義を追加するコードは次のとおりです。

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

4. コンストラクタを更新して、バリデーションのためにプロパティセッターを使用するようにします。これにより、`Stock` クラスの新しいインスタンスが作成されるたびに、`shares` と `price` の値が自動的に検証されます。更新後のコンストラクタは次のとおりです。

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self.shares = shares  # Using property setter
       self.price = price    # Using property setter
   ```

5. これらの変更をすべて加えた後、`stock.py` ファイルを保存します。これにより、変更が保存されます。

6. バリデーションが正しく機能していることを確認するために、テストスクリプトを作成します。次のコマンドを使用してエディタで `test_validation.py` という名前の新しいファイルを開きます。

   ```bash
   code /home/labex/project/test_validation.py
   ```

7. `test_validation.py` ファイルに次のコードを追加します。このコードは、有効な `Stock` インスタンスを作成し、`shares` と `price` 属性を有効および無効な値で更新しようとします。また、結果と発生したエラーメッセージを出力します。

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

8. 最後に、ターミナルで次のコマンドを使用してテストスクリプトを実行します。
   ```bash
   python /home/labex/project/test_validation.py
   ```

有効な更新が成功したことを示す出力と、無効な更新に対する適切なエラーメッセージが表示されるはずです。これにより、プロパティのバリデーションが期待通りに機能していることが確認されます。
