# データをプロットする

このステップでは、Matplotlib の`plot`関数を使って軸オブジェクト上にデータをプロットします。異なる傾きとランダムノイズを持つ 6 つの異なる線をプロットします。

```python
ax.plot(x, np.sin(x) + x + noise)
ax.plot(x, np.sin(x) + 0.5 * x + noise)
ax.plot(x, np.sin(x) + 2 * x + noise)
ax.plot(x, np.sin(x) - 0.5 * x + noise)
ax.plot(x, np.sin(x) - 2 * x + noise)
ax.plot(x, np.sin(x) + noise)
```
