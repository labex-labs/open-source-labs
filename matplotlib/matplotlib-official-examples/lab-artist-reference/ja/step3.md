# 図形の描画

ここでは、Matplotlib を使って `shapes` リストを反復処理し、プロットに追加することで図形を描画します。

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```
