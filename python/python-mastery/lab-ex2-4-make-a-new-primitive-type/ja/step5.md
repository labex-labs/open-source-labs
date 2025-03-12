# 型変換の追加

現在、私たちの `MutInt` クラスは加算と比較演算をサポートしています。しかし、`int()` や `float()` などの Python の組み込み変換関数とは連携していません。これらの変換関数は Python で非常に便利です。たとえば、異なる計算や操作のために値を整数または浮動小数点数に変換したい場合、これらの関数に依存します。そこで、`MutInt` クラスにこれらの関数と連携する機能を追加しましょう。

1. WebIDE で `mutint.py` を開き、次のコードで更新します。

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value

    def __str__(self):
        """Return a string representation for printing."""
        return str(self.value)

    def __repr__(self):
        """Return a developer - friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

`MutInt` クラスに 3 つの新しいメソッドを追加しました。

1. `__int__()`: このメソッドは、`MutInt` クラスのオブジェクトに `int()` 関数を使用するときに呼び出されます。たとえば、`MutInt` オブジェクト `a` があり、`int(a)` と書くと、Python は `a` オブジェクトの `__int__()` メソッドを呼び出します。
2. `__float__()`: 同様に、このメソッドは、`MutInt` オブジェクトに `float()` 関数を使用するときに呼び出されます。
3. `__index__()`: このメソッドは、整数インデックスが必要な操作に使用されます。たとえば、インデックスを使用してリストの要素にアクセスしたり、ビット長操作を行ったりする場合、Python は整数インデックスが必要です。

`__index__` メソッドは、リストのインデックス付け、スライシング、ビット長操作など、整数インデックスを必要とする操作にとって重要です。このシンプルな実装では、`MutInt` オブジェクトの値を直接整数インデックスとして使用できるため、`__index__` を `__int__` と同じに設定しています。

2. これらの新しいメソッドをテストするために、`test_conversions.py` という新しいテストファイルを作成します。

```python
# test_conversions.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test conversions
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Test using as an index
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Test using in bit operations (requires __index__)
print(f"1 << a: {1 << a}")  # Shift left by 3

# Test hex/oct/bin functions (requires __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Modify and test again
a.value = 5
print(f"\nAfter changing value to 5:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. テストスクリプトを実行します。

```bash
python3 /home/labex/project/test_conversions.py
```

次のような出力が表示されるはずです。

```
int(a): 3
float(a): 3.0
names[a]: Paula
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

After changing value to 5:
int(a): 5
names[a]: Lewis
```

これで、`MutInt` クラスは標準の Python 型に変換でき、整数インデックスが必要な操作で使用できるようになりました。

`__index__` メソッドは特に重要です。このメソッドは、リストのインデックス付け、ビット演算、`hex()`、`oct()`、`bin()` などのさまざまな関数のように、整数インデックスが必要な状況でオブジェクトを使用できるようにするために Python で導入されました。

これらの追加により、`MutInt` クラスはかなり完成度の高いプリミティブ型になりました。通常の整数が使用されるほとんどのコンテキストで使用でき、可変であるという追加の利点もあります。

## 完全な MutInt の実装

ここに、追加したすべての機能を含む完全な `MutInt` の実装を示します。

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value

    def __str__(self):
        """Return a string representation for printing."""
        return str(self.value)

    def __repr__(self):
        """Return a developer - friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

この実装は、Python で新しいプリミティブ型を作成する主要な側面を網羅しています。さらに完全なものにするために、減算、乗算、除算などの他の操作に対する追加のメソッドを実装することもできます。
