# 電界を計算する

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

解説:

- `CubicTriInterpolator`は3次多項式を使ってデータを補間するクラスです。
- `tci`は`CubicTriInterpolator`クラスのインスタンスです。
- `(Ex, Ey)`は電界です。
- `E_norm`は正規化された電界です。
