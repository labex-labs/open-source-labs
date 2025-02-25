# Задаем цвета и создаем PatchCollection

Мы задаем цвета фигур и создаем `PatchCollection()`.

```python
colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)
```
