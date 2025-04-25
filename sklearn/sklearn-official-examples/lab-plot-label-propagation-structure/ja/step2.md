# データセットを生成する

次に、`make_circles`を使って 2 つの同心円からなるデータセットを生成します。データセットには、それぞれ外側と内側の円に属する 2 つのサンプルを除いてすべてのサンプルが未知のままであるようにラベルを割り当てます。

```python
n_samples = 200
X, y = make_circles(n_samples=n_samples, shuffle=False)
outer, inner = 0, 1
labels = np.full(n_samples, -1.0)
labels[0] = outer
labels[-1] = inner
```
