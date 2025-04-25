# データの生成

次に、ワイヤーフレームプロットを作成するために使用するデータを生成します。この実験では、`np.meshgrid()`関数を使用して X、Y、および Z 座標を作成します。

```python
# Generate data
X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
