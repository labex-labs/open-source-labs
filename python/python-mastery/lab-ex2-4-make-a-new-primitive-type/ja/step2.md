# 文字列表現の改善

Python で `MutInt` オブジェクトを印刷すると、`<__main__.MutInt object at 0x...>` のような出力が表示されます。この出力は、`MutInt` オブジェクトの実際の値を示していないため、あまり役に立ちません。オブジェクトが表すものを理解しやすくするために、文字列表現用の特殊メソッドを実装します。

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
```

`MutInt` クラスに 3 つの重要なメソッドを追加しました。

- `__str__()`: このメソッドは、オブジェクトに `str()` 関数を使用するとき、またはオブジェクトを直接印刷するときに呼び出されます。人間が読みやすい文字列を返す必要があります。
- `__repr__()`: このメソッドは、オブジェクトの「公式」な文字列表現を提供します。主にデバッグに使用され、理想的には `eval()` 関数に渡すとオブジェクトを再作成できる文字列を返す必要があります。
- `__format__()`: このメソッドにより、`MutInt` オブジェクトで Python の文字列フォーマットシステムを使用できます。パディングや数値フォーマットなどのフォーマット指定を使用できます。

2. これらの新しいメソッドをテストするために、`test_string_repr.py` という新しいテストファイルを作成します。

```python
# test_string_repr.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test string representation
print(f"str(a): {str(a)}")
print(f"repr(a): {repr(a)}")

# Test direct printing
print(f"Print a: {a}")

# Test string formatting
print(f"Formatted with padding: '{a:*^10}'")
print(f"Formatted as decimal: '{a:d}'")

# Test mutability
a.value = 42
print(f"After changing value, repr(a): {repr(a)}")
```

このテストファイルでは、まず `MutInt` クラスをインポートします。次に、値が `3` の `MutInt` オブジェクトを作成します。`str()` と `repr()` 関数を使用して `__str__()` と `__repr__()` メソッドをテストします。また、直接印刷、文字列フォーマット、および `MutInt` オブジェクトの可変性もテストします。

3. テストスクリプトを実行します。

```bash
python3 /home/labex/project/test_string_repr.py
```

このコマンドを実行すると、Python は `test_string_repr.py` スクリプトを実行します。次のような出力が表示されるはずです。

```
str(a): 3
repr(a): MutInt(3)
Print a: 3
Formatted with padding: '****3*****'
Formatted as decimal: '3'
After changing value, repr(a): MutInt(42)
```

これで、`MutInt` オブジェクトが見やすく表示されるようになりました。文字列表現には基になる値が表示され、通常の整数と同じように文字列フォーマットを使用できます。

`__str__()` と `__repr__()` の違いは、`__str__()` は人間が読みやすい出力を生成することを目的としているのに対し、`__repr__()` は理想的には `eval()` に渡すとオブジェクトを再作成できる文字列を生成する必要があるということです。このため、`__repr__()` メソッドにクラス名を含めました。

`__format__()` メソッドにより、オブジェクトが Python のフォーマットシステムと連携できるようになり、パディングや数値フォーマットなどのフォーマット指定を使用できます。
