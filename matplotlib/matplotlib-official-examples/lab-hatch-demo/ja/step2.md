# データの作成

次に、グラフに使用するデータを作成する必要があります。この場合、NumPy ライブラリを使用して 2 つの配列を作成します。

```python
x = np.arange(1, 5)
y1 = np.arange(1, 5)
y2 = np.ones(y1.shape) * 4
```
