# データの生成

次に、プロットするためのデータを生成する必要があります。この例では、3 つの配列を作成します。1 つは x 軸の値用、1 つは最初のプロットの y 軸の値用、そして 1 つは 3 番目のプロットの y 軸の値用です。

```python
dt = 0.01
x = np.arange(-50.0, 50.0, dt)
y1 = np.arange(0, 100.0, dt)
y3 = np.sin(x / 3.0)
```
