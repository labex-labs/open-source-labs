# データをプロットする

サブプロットを作成したので、`np.sin(x)` を使ってデータをプロットできます。

```python
x = np.arange(0, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.sin(x))
```
