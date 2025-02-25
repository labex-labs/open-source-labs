# フォーマッターにコール可能オブジェクトを使用する

`.Axis.set_major_formatter` に関数を渡す代わりに、`__call__` を実装するクラスのインスタンスなど、他のコール可能オブジェクトを使用することができます。このステップでは、目盛りを日付にフォーマットする `MyFormatter` クラスを作成します。

```python
# Use a callable for formatter
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """Return the label for time x at position pos."""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass

ax2.xaxis.set_major_formatter(MyFormatter(r.date, '%a'))
```
