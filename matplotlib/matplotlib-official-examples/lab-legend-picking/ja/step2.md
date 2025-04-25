# データを準備する

NumPy を使って、異なる周波数の 2 つのサイン波を生成します。

```python
t = np.linspace(0, 1)
y1 = 2 * np.sin(2*np.pi*t)
y2 = 4 * np.sin(2*np.pi*2*t)
```
