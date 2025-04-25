# 変換関数を定義する

2 番目のステップは、変換関数を定義することです。この例では、x 軸の値を変換して y 軸の値は変更しないために`tr`関数を使用します。`inv_tr`関数は、変換を逆にするために使用されます。

```python
def tr(x, y):
    return np.sign(x)*abs(x)**.5, y

def inv_tr(x, y):
    return np.sign(x)*x**2, y
```
