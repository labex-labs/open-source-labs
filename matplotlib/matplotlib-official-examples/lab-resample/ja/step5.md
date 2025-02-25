# 信号の作成

NumPy を使って信号を作成します。start=16、stop=365、num=(365-16)\*4 として linspace 関数を使って配列 xdata を作成します。sin 関数と cos 関数を使って配列 ydata を作成します。

```python
xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2*np.pi*xdata/153) + np.cos(2*np.pi*xdata/127)
```
