# データの生成

次に、プロット用のデータを生成します。`numpy`を使って、異なる周波数の 3 つのサイン波を作成します。

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(6*np.pi*t)
```
