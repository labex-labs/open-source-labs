# ランダムなデータセットの作成

このステップでは、ランダムなデータセットを作成します。0 から 200 までのランダムな値を持つ 100 要素のソート済み配列を作成するために`numpy`ライブラリを使用し、その後、各要素から 100 を引きます。次に、`numpy`を使って各要素のサインとコサインを計算し、これらの配列を形状 (100, 2) の 2 次元配列に結合して`y`配列を作成します。また、5 番目の要素にランダムノイズを追加します。

```python
# Create a random dataset
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(100, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y[::5, :] += 0.5 - rng.rand(20, 2)
```
