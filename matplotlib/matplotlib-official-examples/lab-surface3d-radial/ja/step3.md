# 直交座標系でメッシュを表す

次に、NumPy の `cos()` と `sin()` 関数を使って、直交座標系でメッシュを表します。

```python
X, Y = R*np.cos(P), R*np.sin(P)
```
