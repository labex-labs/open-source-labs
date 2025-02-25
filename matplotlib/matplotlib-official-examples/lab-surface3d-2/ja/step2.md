# データの作成

次のステップは、3D 曲面用のデータを作成することです。`u`、`v`、`x`、`y`、`z` を定義する必要があります。これらの変数は、曲面を描画するために必要な角度と座標を表します。NumPy の `linspace()` 関数を使って角度を作成し、`outer()` 関数を使って座標を作成します。

```python
# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
```
