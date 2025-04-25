# データを作成する

次に、プロットで使用するデータを作成します。`numpy` ライブラリを使って、異なる周波数の 3 つの異なるサイン波を作成します。

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)
```
