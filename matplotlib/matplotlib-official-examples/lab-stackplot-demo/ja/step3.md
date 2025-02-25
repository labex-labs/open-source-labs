# ストリームグラフの作成

3番目のステップは、`baseline`パラメータを'wiggle'に設定した`stackplot()`関数を使ってストリームグラフを作成することです。ガウス分布のランダムな混合物を作成し、それらをストリームグラフとして描画します。

```python
# 再現性のための乱数シードの固定
np.random.seed(19680801)


def gaussian_mixture(x, n=5):
    """位置 *x* で評価される *n* 個のガウス分布のランダムな混合物を返す。"""
    def add_random_gaussian(a):
        amplitude = 1 / (.1 + np.random.random())
        dx = x[-1] - x[0]
        x0 = (2 * np.random.random() -.5) * dx
        z = 10 / (.1 + np.random.random()) / dx
        a += amplitude * np.exp(-(z * (x - x0))**2)
    a = np.zeros_like(x)
    for j in range(n):
        add_random_gaussian(a)
    return a


x = np.linspace(0, 100, 101)
ys = [gaussian_mixture(x) for _ in range(3)]

fig, ax = plt.subplots()
ax.stackplot(x, ys, baseline='wiggle')
plt.show()
```
