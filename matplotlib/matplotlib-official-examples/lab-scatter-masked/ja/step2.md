# 散布図用のデータの生成

次に、散布図用のデータを生成します。0 から 0.9 までのランダムな x と y の値と、0 から 10 までのランダムな半径を持つ 100 個のデータポイントを作成します。各データポイントの色は、その面積の平方根によって決まります。

```python
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
c = np.sqrt(area)
```
