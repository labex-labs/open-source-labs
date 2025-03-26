# 型変換の追加

現在の `MutInt` クラスは、加算と比較の操作をサポートしています。しかし、Python の組み込み変換関数である `int()` や `float()` とは連携しません。これらの変換関数は Python では非常に便利です。たとえば、さまざまな計算や操作のために値を整数または浮動小数点数に変換したい場合、これらの関数に頼ることになります。そこで、`MutInt` クラスにこれらの関数と連携する機能を追加しましょう。

1. WebIDE で `mutint.py` を開き、以下のコードで更新します。

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    作成後に値を変更できる可変整数クラス。
    """
    __slots__ = ['value']

    def __init__(self, value):
        """整数値で初期化します。"""
        self.value = value

    def __str__(self):
        """印刷用の文字列表現を返します。"""
        return str(self.value)

    def __repr__(self):
        """開発者向けの文字列表現を返します。"""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """書式指定による文字列の書式設定をサポートします。"""
        return format(self.value, fmt)

    def __add__(self, other):
        """加算を処理します：self + other。"""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """逆加算を処理します：other + self。"""
        return self.__add__(other)

    def __iadd__(self, other):
        """インプレース加算を処理します：self += other。"""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """等価比較を処理します：self == other。"""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """より小さい比較を処理します：self < other。"""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """int に変換します。"""
        return self.value

    def __float__(self):
        """float に変換します。"""
        return float(self.value)

    __index__ = __int__  # 配列のインデックス操作や、インデックスを必要とするその他の操作をサポートします

    def __lshift__(self, other):
        """左シフトを処理します：self << other。"""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """逆左シフトを処理します：other << self。"""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

`MutInt` クラスに 3 つの新しいメソッドを追加しました。

1. `__int__()`: このメソッドは、`MutInt` クラスのオブジェクトに対して `int()` 関数を使用すると呼び出されます。たとえば、`MutInt` オブジェクト `a` があり、`int(a)` と記述すると、Python は `a` オブジェクトの `__int__()` メソッドを呼び出します。
2. `__float__()`: 同様に、このメソッドは、`MutInt` オブジェクトに対して `float()` 関数を使用すると呼び出されます。
3. `__index__()`: このメソッドは、特に整数インデックスを必要とする操作に使用されます。たとえば、インデックスを使用してリスト内の要素にアクセスしたり、ビット長操作を実行したりする場合、Python は整数インデックスを必要とします。
4. `__lshift__()`: このメソッドは、`MutInt` オブジェクトが `<<` 演算子の左側にある場合に、左シフト演算を処理します。
5. `__rlshift__()`: このメソッドは、`MutInt` オブジェクトが `<<` 演算子の右側にある場合に、左シフト演算を処理します。

`__index__` メソッドは、リストのインデックス操作、スライス、ビット長操作など、整数インデックスを必要とする操作にとって非常に重要です。この簡単な実装では、`MutInt` オブジェクトの値は整数インデックスとして直接使用できるため、`__int__` と同じになるように設定しました。

`__lshift__` および `__rlshift__` メソッドは、ビット単位の左シフト演算をサポートするために不可欠です。これらにより、`MutInt` オブジェクトはビット単位の演算に参加できるようになります。これは、整数のような型によくある要件です。

2. これらの新しいメソッドをテストするために、`test_conversions.py` という名前の新しいテストファイルを作成します。

```python
# test_conversions.py

from mutint import MutInt

# MutInt オブジェクトを作成します
a = MutInt(3)

# 変換をテストします
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# インデックスとして使用してテストします
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# ビット演算で使用してテストします (__index__ が必要です)
print(f"1 << a: {1 << a}")  # 3 だけ左にシフトします

# hex/oct/bin 関数を使用してテストします (__index__ が必要です)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# 変更して再度テストします
a.value = 4
print(f"\n値を 4 に変更した後：")
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
names[a]: Thomas
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

値を 4 に変更した後:
int(a): 4
names[a]: Lewis
```

これで、`MutInt` クラスは標準の Python 型に変換でき、整数インデックスを必要とする操作で使用できます。

`__index__` メソッドは特に重要です。これは、リストのインデックス操作、ビット単位の演算、`hex()`、`oct()`、`bin()` などのさまざまな関数など、整数インデックスが必要な状況でオブジェクトを使用できるようにするために Python で導入されました。

これらの追加により、`MutInt` クラスはかなり完全なプリミティブ型になりました。通常の整数が使用されるほとんどのコンテキストで使用でき、可変であるという利点が追加されています。

## 完全な MutInt の実装

以下は、追加したすべての機能を備えた完全な `MutInt` の実装です。

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    作成後に値を変更できる可変整数クラス。
    """
    __slots__ = ['value']

    def __init__(self, value):
        """整数値で初期化します。"""
        self.value = value

    def __str__(self):
        """印刷用の文字列表現を返します。"""
        return str(self.value)

    def __repr__(self):
        """開発者向けの文字列表現を返します。"""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """書式指定による文字列の書式設定をサポートします。"""
        return format(self.value, fmt)

    def __add__(self, other):
        """加算を処理します：self + other。"""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """逆加算を処理します：other + self。"""
        return self.__add__(other)

    def __iadd__(self, other):
        """インプレース加算を処理します：self += other。"""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """等価比較を処理します：self == other。"""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """より小さい比較を処理します：self < other。"""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """int に変換します。"""
        return self.value

    def __float__(self):
        """float に変換します。"""
        return float(self.value)

    __index__ = __int__  # 配列のインデックス操作や、インデックスを必要とするその他の操作をサポートします

    def __lshift__(self, other):
        """左シフトを処理します：self << other。"""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """逆左シフトを処理します：other << self。"""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

この実装は、Python で新しいプリミティブ型を作成する際の重要な側面を網羅しています。さらに完全にするには、減算、乗算、除算などの他の操作のためのメソッドを追加で実装できます。
