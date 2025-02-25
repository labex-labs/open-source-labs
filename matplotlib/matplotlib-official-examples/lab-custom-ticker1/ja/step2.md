# カスタム チェッカー関数を定義する

次に、カスタム チェッカー関数を定義する必要があります。カスタム チェッカー関数は 2 つの引数（値と目盛り位置）をとり、フォーマットされた目盛りラベルを返します。この場合、目盛りラベルを数百万ドルでフォーマットします。

```python
def millions(x, pos):
    """The two arguments are the value and tick position."""
    return f'${x*1e-6:1.1f}M'
```
