# 点のサイズと色を定義する

このステップでは、散布図の点のサイズと色を定義します。点のサイズと色について乱数値を生成するために、NumPy ライブラリを使用します。

```python
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2
```
