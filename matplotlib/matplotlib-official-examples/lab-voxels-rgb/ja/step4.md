# 色の結合

次に、RGB色コンポーネントを形状が`(17, 17, 17, 3)`の単一の配列に結合します。

```python
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc
```
