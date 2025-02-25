# データの作成

次に、風羽図を生成するために使用するデータを作成します。5x5の一様なグリッドと、meshgrid関数と乗算関数を使ってベクトル場を作成します。

```python
x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y
```
