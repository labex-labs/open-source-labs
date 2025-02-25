# データポイントの作成

このステップでは、カスタム単位クラス - `Foo` を使用していくつかのデータポイントを作成します。

```python
# create some Foos
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# and some arbitrary y data
y = [i for i in range(len(x))]
```
