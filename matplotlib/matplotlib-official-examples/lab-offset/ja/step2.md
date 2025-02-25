# データを作成する

次に、プロットで使用するデータを作成します。この例では、NumPy を使ってデータを生成します。

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
```
