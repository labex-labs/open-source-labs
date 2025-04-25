# データを設定する

NumPy ライブラリを使って、ランダムな値を持つ 2 セットのデータを生成します。1 セットは x 座標と y 座標を表し、もう 1 セットは z 座標を表します。

```python
def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
```
