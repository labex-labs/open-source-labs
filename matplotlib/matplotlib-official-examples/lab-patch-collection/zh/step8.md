# 设置颜色并创建PatchCollection

我们设置形状的颜色并创建一个 `PatchCollection()`。

```python
colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)
```
