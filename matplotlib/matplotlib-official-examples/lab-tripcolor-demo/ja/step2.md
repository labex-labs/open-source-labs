# デロネ三角分割の作成

点群のデロネ三角分割を作成します。まず、NumPy を使って点群の x 座標と y 座標を作成します。

```python
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)
angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles
x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
```

次に、点群の z 座標を作成します。

```python
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
```

次に、`matplotlib.tri` の `Triangulation()` 関数を使って Triangulation オブジェクトを作成します。三角形を指定しないため、自動的にデロネ三角分割が作成されます。

```python
triang = tri.Triangulation(x, y)
```

最後に、`set_mask()` 関数を使って不要な三角形をマスクします。この例では、平均半径が `min_radius` 未満の三角形を除外するようにマスクを設定しています。

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
