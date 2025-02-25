# バーグラフ用のデータの生成

次に、バーグラフ用のデータを生成します。4 セットのデータを作成し、それぞれに 20 個の値を持たせます。20 個の値の配列を作成するために NumPy の `arange()` メソッドを、各セットのデータに乱数を生成するために NumPy の `random.rand()` メソッドを使用します。

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```
