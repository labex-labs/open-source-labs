# 追加の余白付きの散布図

このステップでは、丸い数のオートリミットモードが依然として維持されたまま、`.Axes.set_xmargin` / `.Axes.set_ymargin` を使用してデータの周りに追加の余白を設定します。

```python
fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
ax.set_xmargin(0.8)
plt.show()
```
