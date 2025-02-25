# データを生成する

次に、サンプルデータを生成します。この実験では、2次元のサイン波を生成します。

```python
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
```
