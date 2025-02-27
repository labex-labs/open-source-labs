# ランダムなデータセットの作成

次に、回帰に使用するランダムなデータセットを作成します。`numpy`を使って、-100から100までの600個のx値のセットを作成し、x値のサインとコサインに基づいて計算される対応するy値にいくらかのランダムノイズを加えます。

```python
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(600, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y += 0.5 - rng.rand(*y.shape)
```
