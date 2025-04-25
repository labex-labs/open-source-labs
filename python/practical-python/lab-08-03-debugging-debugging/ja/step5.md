# Python デバッガ

プログラム内でデバッガを手動で起動することができます。

```python
def some_function():
 ...
    breakpoint()      # デバッガに入る (Python 3.7 以降)
 ...
```

これにより、`breakpoint()` の呼び出し箇所でデバッガが起動します。

以前の Python バージョンでは、このようにしていました。他のデバッグガイドでこれが言及されることもあります。

```python
import pdb
...
pdb.set_trace()       # `breakpoint()` の代わり
...
```
