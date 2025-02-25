# 関数の定義

このステップでは、減衰振動を生成する関数を定義します。

```python
def f(t):
    return np.cos(2*np.pi*t) * np.exp(-t)
```
