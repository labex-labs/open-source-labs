# 比較演算の実装

現在、私たちの `MutInt` オブジェクトは、互いに比較することも、通常の整数と比較することもできません。Python では、`==`、`<`、`<=`、`>`、`>=` などの比較演算は、オブジェクトを操作する際に非常に便利です。これらの演算により、異なるオブジェクト間の関係を判断でき、ソート、フィルタリング、条件文などの多くのプログラミングシナリオで重要です。そこで、比較演算の特殊メソッドを実装して、`MutInt` クラスに比較機能を追加しましょう。

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

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less-than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
```

いくつかの重要な改良を加えました。

1. `functools` モジュールから `@total_ordering` デコレータをインポートして使用します。`@total_ordering` デコレータは Python の強力なツールです。クラスの比較メソッドを実装する際に、多くの時間と労力を節約できます。6 つの比較メソッド（`__eq__`、`__ne__`、`__lt__`、`__le__`、`__gt__`、`__ge__`）を手動で定義する代わりに、`__eq__` ともう 1 つの比較メソッド（この場合は `__lt__`）を定義するだけで済みます。デコレータは自動的に残りの 4 つの比較メソッドを生成します。
2. 等価比較（`==`）を処理する `__eq__()` メソッドを追加します。このメソッドは、2 つの `MutInt` オブジェクト、または `MutInt` オブジェクトと整数が同じ値を持っているかをチェックするために使用されます。
3. 小なり比較（`<`）を処理する `__lt__()` メソッドを追加します。このメソッドは、1 つの `MutInt` オブジェクト、または `MutInt` オブジェクトと整数を比較した場合に、値が小さいかどうかを判断するために使用されます。

4. これらの新しいメソッドをテストするために、`test_comparisons.py` という新しいテストファイルを作成します。

```python
# test_comparisons.py

from mutint import MutInt

# Create MutInt objects
a = MutInt(3)
b = MutInt(3)
c = MutInt(5)

# Test equality
print(f"a == b: {a == b}")  # Should be True (same value)
print(f"a == c: {a == c}")  # Should be False (different values)
print(f"a == 3: {a == 3}")  # Should be True (comparing with int)
print(f"a == 5: {a == 5}")  # Should be False (different values)

# Test less than
print(f"a < c: {a < c}")    # Should be True (3 < 5)
print(f"c < a: {c < a}")    # Should be False (5 is not < 3)
print(f"a < 4: {a < 4}")    # Should be True (3 < 4)

# Test other comparisons (provided by @total_ordering)
print(f"a <= b: {a <= b}")  # Should be True (3 <= 3)
print(f"a > c: {a > c}")    # Should be False (3 is not > 5)
print(f"c >= a: {c >= a}")  # Should be True (5 >= 3)

# Test with a different type
print(f"a == '3': {a == '3'}")  # Should be False (different types)
```

このテストファイルでは、いくつかの `MutInt` オブジェクトを作成し、それらに対してさまざまな比較演算を実行します。また、`MutInt` オブジェクトを通常の整数や異なる型（この場合は文字列）と比較します。これらのテストを実行することで、比較メソッドが期待通りに動作することを確認できます。

3. テストスクリプトを実行します。

```bash
python3 /home/labex/project/test_comparisons.py
```

次のような出力が表示されるはずです。

```
a == b: True
a == c: False
a == 3: True
a == 5: False
a < c: True
c < a: False
a < 4: True
a <= b: True
a > c: False
c >= a: True
a == '3': False
```

これで、`MutInt` クラスはすべての比較演算をサポートするようになりました。

`@total_ordering` デコレータは、6 つの比較メソッドを手動で実装する必要がないため、特に便利です。`__eq__` と `__lt__` を提供するだけで、Python は他の 4 つの比較メソッドを自動的に導出できます。

カスタムクラスを実装する際には、通常、同じ型のオブジェクトと組み込み型の両方で動作するようにするのが良い習慣です。そのため、比較メソッドは `MutInt` オブジェクトと通常の整数の両方を処理します。これにより、`MutInt` クラスはさまざまなプログラミングシナリオでより柔軟に使用できます。
