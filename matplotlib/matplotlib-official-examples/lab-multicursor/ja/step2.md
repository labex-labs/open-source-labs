# データの作成

次に、プロット用のデータを作成します。この例では、異なる周波数の3つのサイン波を作成します。

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(3*np.pi*t)
s3 = np.sin(4*np.pi*t)
```
