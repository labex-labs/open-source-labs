# なぜ `super()` を使うのか

メソッドをオーバーライドする際は常に `super()` を使用します。

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` は、MRO 上の _次のクラス_ に委譲します。

厄介なことに、それが何であるかはわかりません。特に多重継承が使われている場合、それが何であるかはわかりません。
