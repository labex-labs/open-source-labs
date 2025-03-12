# コード生成器としてのクロージャ

このステップでは、クロージャ (Closure) を使ってコードを動的に生成する方法を学びます。具体的には、クロージャを使ってクラス属性の型チェック (type-checking) システムを構築します。

まず、クロージャが何であるかを理解しましょう。クロージャは、メモリ上に存在しなくても、外側のスコープの値を記憶する関数オブジェクトです。Python では、ネストされた関数が外側の関数の値を参照するときにクロージャが作成されます。

では、型チェックシステムの実装を始めましょう。

1. `/home/labex/project` ディレクトリに `typedproperty.py` という名前の新しいファイルを作成し、以下のコードを記述します。

```python
# typedproperty.py

def typedproperty(name, expected_type):
    """
    Create a property with type checking.

    Args:
        name: The name of the property
        expected_type: The expected type of the property value

    Returns:
        A property object that performs type checking
    """
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

このコードでは、`typedproperty` 関数がクロージャです。この関数は `name` と `expected_type` という 2 つの引数を受け取ります。`@property` デコレータは、プロパティのゲッターメソッドを作成するために使用され、これにより非公開属性の値が取得されます。`@value.setter` デコレータは、設定される値が期待される型であるかをチェックするセッターメソッドを作成します。もしそうでなければ、`TypeError` が発生します。

2. これらの型付きプロパティを使用するクラスを作成しましょう。以下のコードで `stock.py` という名前のファイルを作成します。

```python
from typedproperty import typedproperty

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

`Stock` クラスでは、`typedproperty` 関数を使用して `name`、`shares`、`price` の型チェック付き属性を作成しています。`Stock` クラスのインスタンスを作成すると、型チェックが自動的に適用されます。

3. これを実際に動作させるためのテストファイルを作成しましょう。以下のコードで `test_stock.py` という名前のファイルを作成します。

```python
from stock import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.shares = "hundred"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

このテストファイルでは、まず正しい型で `Stock` オブジェクトを作成します。次に、`shares` 属性を文字列に設定しようとしますが、期待される型は整数なので `TypeError` が発生するはずです。

4. テストファイルを実行します。

```bash
python3 test_stock.py
```

以下のような出力が表示されるはずです。

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'int'>
```

この出力は、型チェックが正しく動作していることを示しています。

5. 次に、`typedproperty.py` を拡張して、一般的な型のための便利関数を追加しましょう。ファイルの末尾に以下のコードを追加します。

```python
def String(name):
    """Create a string property with type checking."""
    return typedproperty(name, str)

def Integer(name):
    """Create an integer property with type checking."""
    return typedproperty(name, int)

def Float(name):
    """Create a float property with type checking."""
    return typedproperty(name, float)
```

これらの関数は `typedproperty` 関数をラップしたもので、一般的な型のプロパティを簡単に作成できるようにしています。

6. これらの便利関数を使用する `stock_enhanced.py` という名前の新しいファイルを作成します。

```python
from typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

この `Stock` クラスは、便利関数を使用して型チェック付き属性を作成しており、コードがより読みやすくなっています。

7. 拡張版をテストするための `test_stock_enhanced.py` という名前のテストファイルを作成します。

```python
from stock_enhanced import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.price = "490.1"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

このテストファイルは前のものと似ていますが、拡張版の `Stock` クラスをテストしています。

8. テストを実行します。

```bash
python3 test_stock_enhanced.py
```

以下のような出力が表示されるはずです。

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'float'>
```

このステップでは、クロージャを使ってコードを生成する方法を実証しました。`typedproperty` 関数は型チェックを行うプロパティオブジェクトを作成し、`String`、`Integer`、`Float` 関数は一般的な型の特殊なプロパティを作成します。
