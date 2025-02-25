# ランダムなデータを生成する

NumPy を使って散布図用のランダムなデータを生成します。ランダムな半径と角度の値を持つ 150 個のデータポイントを作成し、各ポイントの面積と色を計算します。

```python
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
```
