# データの生成

このステップでは、`numpy.random.RandomState`関数とステップ3で定義されたパラメータを使用してデータを生成します。

```python
rng = np.random.RandomState(random_state)
X = np.vstack(
    [
        rng.multivariate_normal(means[j], covars[j], samples[j])
        for j in range(n_components)
    ]
)
y = np.concatenate([np.full(samples[j], j, dtype=int) for j in range(n_components)])
```
