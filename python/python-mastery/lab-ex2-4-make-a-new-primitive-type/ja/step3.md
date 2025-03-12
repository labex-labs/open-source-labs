# 数学的演算の追加

現在、私たちの `MutInt` クラスは加算などの数学的演算をサポートしていません。Python では、カスタムクラスにこのような演算を有効にするには、特殊メソッドを実装する必要があります。これらの特殊メソッドは、二重アンダースコアで囲まれているため、「マジックメソッド」または「ダンダーメソッド」とも呼ばれます。算術演算に関連する特殊メソッドを実装して、加算機能を追加しましょう。

1. WebIDE で `mutint.py` を開き、次のコードで更新します。

```python
# mutint.py

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
        """Return a developer-friendly string representation."""
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
        # For commutative operations like +, we can reuse __add__
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in-place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

`MutInt` クラスに 3 つの新しいメソッドを追加しました。

- `__add__()`: このメソッドは、`+` 演算子が左側に `MutInt` オブジェクトを持つ場合に呼び出されます。このメソッド内では、まず `other` オペランドが `MutInt` のインスタンスまたは `int` であるかを確認します。もしそうであれば、加算を実行し、結果を持つ新しい `MutInt` オブジェクトを返します。`other` オペランドがそれ以外の場合は、`NotImplemented` を返します。これは、Python に他のメソッドを試すか、`TypeError` を発生させるよう指示します。
- `__radd__()`: このメソッドは、`+` 演算子が右側に `MutInt` オブジェクトを持つ場合に呼び出されます。加算は可換演算（つまり、`a + b` は `b + a` と同じ）であるため、`__add__` メソッドを再利用できます。
- `__iadd__()`: このメソッドは、`+=` 演算子が `MutInt` オブジェクトに使用された場合に呼び出されます。新しいオブジェクトを作成する代わりに、既存の `MutInt` オブジェクトを変更して返します。

2. これらの新しいメソッドをテストするために、`test_math_ops.py` という新しいテストファイルを作成します。

```python
# test_math_ops.py

from mutint import MutInt

# Create MutInt objects
a = MutInt(3)
b = MutInt(5)

# Test regular addition
c = a + b
print(f"a + b = {c}")

# Test addition with int
d = a + 10
print(f"a + 10 = {d}")

# Test reversed addition
e = 7 + a
print(f"7 + a = {e}")

# Test in-place addition
print(f"Before a += 5: a = {a}")
a += 5
print(f"After a += 5: a = {a}")

# Test in-place addition with reference sharing
f = a  # f and a point to the same object
print(f"Before a += 10: a = {a}, f = {f}")
a += 10
print(f"After a += 10: a = {a}, f = {f}")

# Test unsupported operation
try:
    result = a + 3.5  # Adding a float is not supported
    print(f"a + 3.5 = {result}")
except TypeError as e:
    print(f"Error when adding float: {e}")
```

このテストファイルでは、まず `MutInt` クラスをインポートします。次に、いくつかの `MutInt` オブジェクトを作成し、さまざまな種類の加算演算を実行します。また、インプレース加算と、サポートされていない演算（浮動小数点数の加算）を試みた場合もテストします。

3. テストスクリプトを実行します。

```bash
python3 /home/labex/project/test_math_ops.py
```

次のような出力が表示されるはずです。

```
a + b = MutInt(8)
a + 10 = MutInt(13)
7 + a = MutInt(10)
Before a += 5: a = MutInt(3)
After a += 5: a = MutInt(8)
Before a += 10: a = MutInt(8), f = MutInt(8)
After a += 10: a = MutInt(18), f = MutInt(18)
Error when adding float: unsupported operand type(s) for +: 'MutInt' and 'float'
```

これで、`MutInt` クラスは基本的な加算演算をサポートするようになりました。`+=` を使用したときに、`a` と `f` の両方が更新されたことに注意してください。これは、`a += 10` が新しいオブジェクトを作成するのではなく、既存のオブジェクトを変更したことを示しています。

この可変オブジェクトの動作は、Python の組み込み可変型（リストなど）と似ています。例えば：

```python
a = [1, 2, 3]
b = a
a += [4, 5]  # Both a and b are updated
```

対照的に、タプルなどの不変型の場合、`+=` は新しいオブジェクトを作成します。

```python
c = (1, 2, 3)
d = c
c += (4, 5)  # c is a new object, d still points to the old one
```
