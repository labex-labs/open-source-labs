# 軸の共有

デフォルトでは、各`Axes`は個別にスケーリングされます。サブプロットの水平軸または垂直軸を整列させるには、`sharex`または`sharey`パラメータを使用できます。

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, y)
ax2.plot(x + 1, -y)
```
