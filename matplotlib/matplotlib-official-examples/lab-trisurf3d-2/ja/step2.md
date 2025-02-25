# メッシュを作成する

パラメータ化変数 `u` と `v` の空間にメッシュを作成します。これは、`u` と `v` の点のグリッドを作成するために `np.meshgrid()` 関数を使って行われます。

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```
