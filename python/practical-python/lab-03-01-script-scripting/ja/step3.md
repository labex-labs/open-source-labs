# 定義

名前は、後で使用される前に必ず定義する必要があります。

```python
def square(x):
    return x*x

a = 42
b = a + 2     # `a` が定義されていることが必要です

z = square(b) # `square` と `b` が定義されていることが必要です
```

**順序は重要です。** ほとんどの場合、変数や関数の定義を一番上に近付けます。
