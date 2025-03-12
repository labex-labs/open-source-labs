# ディスクリプタを使ったプロパティ名の冗長性の排除

前のステップで型付きプロパティを作成する際、プロパティ名を明示的に指定する必要がありました。これは、クラス定義ですでにプロパティ名が指定されているため、冗長です。このステップでは、ディスクリプタ (Descriptor) を使ってこの冗長性を排除します。

Python のディスクリプタは、属性アクセスの動作を制御する特殊なオブジェクトです。ディスクリプタに `__set_name__` メソッドを実装すると、クラス定義から自動的に属性名を取得できます。

新しいファイルを作成して始めましょう。

1. 以下のコードで `improved_typedproperty.py` という名前の新しいファイルを作成します。

```python
# improved_typedproperty.py

class TypedProperty:
    """
    A descriptor that performs type checking.

    This descriptor automatically captures the attribute name from the class definition.
    """
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # This method is called when the descriptor is assigned to a class attribute
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

# Convenience functions
def String():
    """Create a string property with type checking."""
    return TypedProperty(str)

def Integer():
    """Create an integer property with type checking."""
    return TypedProperty(int)

def Float():
    """Create a float property with type checking."""
    return TypedProperty(float)
```

このコードは、属性に割り当てられる値の型をチェックする `TypedProperty` というディスクリプタクラスを定義しています。`__set_name__` メソッドは、ディスクリプタがクラス属性に割り当てられると自動的に呼び出されます。これにより、手動で指定することなく属性名を取得できます。

次に、これらの改良された型付きプロパティを使用するクラスを作成します。

2. 改良された型付きプロパティを使用する `stock_improved.py` という名前の新しいファイルを作成します。

```python
from improved_typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    # No need to specify property names anymore
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

型付きプロパティを作成する際に、プロパティ名を指定する必要がないことに注意してください。ディスクリプタはクラス定義から自動的に属性名を取得します。

では、改良されたクラスをテストしましょう。

3. 改良版をテストするための `test_stock_improved.py` という名前のテストファイルを作成します。

```python
from stock_improved import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try setting attributes with wrong types
try:
    s.name = 123  # Should raise TypeError
    print("Name type check failed")
except TypeError as e:
    print(f"Name type check succeeded: {e}")

try:
    s.shares = "hundred"  # Should raise TypeError
    print("Shares type check failed")
except TypeError as e:
    print(f"Shares type check succeeded: {e}")

try:
    s.price = "490.1"  # Should raise TypeError
    print("Price type check failed")
except TypeError as e:
    print(f"Price type check succeeded: {e}")
```

最後に、すべてが期待通りに動作するかどうかを確認するためにテストを実行します。

4. テストを実行します。

```bash
python3 test_stock_improved.py
```

以下のような出力が表示されるはずです。

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Name type check succeeded: Expected <class 'str'>
Shares type check succeeded: Expected <class 'int'>
Price type check succeeded: Expected <class 'float'>
```

このステップでは、ディスクリプタと `__set_name__` メソッドを使って型チェックシステムを改善しました。これにより、冗長なプロパティ名の指定が不要になり、コードが短くなり、エラーが発生する可能性も低くなります。

`__set_name__` メソッドはディスクリプタの非常に便利な機能です。これにより、ディスクリプタはクラス定義での使用方法に関する情報を自動的に収集できます。これは、理解しやすく使いやすい API を作成するために利用できます。
