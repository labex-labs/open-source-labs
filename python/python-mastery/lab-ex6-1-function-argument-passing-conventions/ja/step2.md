# 構造体の基底クラスを作成する

これで関数引数の渡し方を理解したので、データ構造用の再利用可能な基底クラスを作成します。このステップは非常に重要です。データを保持する単純なクラスを作成する際に、同じコードを何度も書くのを避けることができるからです。基底クラスを使用することで、コードを簡素化し、効率的にすることができます。

## 繰り返しコードの問題

前の演習では、以下のように `Stock` クラスを定義しました。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

`__init__` メソッドをよく見ると、かなり繰り返しが多いことがわかります。各属性を手動で 1 つずつ割り当てる必要があります。特に多くの属性を持つクラスが多数ある場合、これは非常に面倒で時間がかかる作業になります。

## 柔軟な基底クラスを作成する

属性の割り当てを自動的に処理できる `Structure` 基底クラスを作成しましょう。まず、WebIDE を開き、`structure.py` という名前の新しいファイルを作成します。次に、以下のコードをこのファイルに追加します。

```python
# structure.py

class Structure:
    """
    A base class for creating simple data structures.
    Automatically populates object attributes from _fields and constructor arguments.
    """
    _fields = ()

    def __init__(self, *args):
        # Check that the number of arguments matches the number of fields
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        # Set the attributes
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```

この基底クラスにはいくつかの重要な特徴があります。

1. `_fields` クラス変数を定義しています。デフォルトでは、この変数は空です。この変数は、クラスが持つ属性の名前を保持します。
2. コンストラクタに渡された引数の数が `_fields` で定義されたフィールドの数と一致するかどうかをチェックします。一致しない場合は、`TypeError` を発生させます。これにより、エラーを早期に検出することができます。
3. フィールド名と引数として提供された値を使用して、オブジェクトの属性を設定します。`setattr` 関数を使用して属性を動的に設定します。

## 構造体の基底クラスをテストする

では、`Structure` 基底クラスを継承するいくつかのサンプルクラスを作成しましょう。`structure.py` ファイルに以下のコードを追加します。

```python
# Example classes using Structure
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

実装が正しく動作するかどうかをテストするために、`test_structure.py` という名前のテストファイルを作成します。このファイルに以下のコードを追加します。

```python
# test_structure.py
from structure import Stock, Point, Date

# Test Stock class
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}, shares: {s.shares}, price: {s.price}")

# Test Point class
p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")

# Test Date class
d = Date(2023, 11, 9)
print(f"Date: {d.year}-{d.month}-{d.day}")

# Test error handling
try:
    s2 = Stock('AAPL', 50)  # Missing price argument
    print("This should not print")
except TypeError as e:
    print(f"Error correctly caught: {e}")
```

テストを実行するには、ターミナルを開き、以下のコマンドを実行します。

```bash
python3 test_structure.py
```

以下の出力が表示されるはずです。

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

ご覧の通り、基底クラスは期待通りに動作しています。同じ定型コードを繰り返し書くことなく、新しいデータ構造を定義するのがはるかに簡単になりました。
