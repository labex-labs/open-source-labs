# プロットの作成

これで、`matplotlib`を使ってプロットを作成し、`Axes`オブジェクトの`add_collection`メソッドを使って`LineCollection`オブジェクトをプロットに追加できます。

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Line collection with masked arrays')
plt.show()
```
