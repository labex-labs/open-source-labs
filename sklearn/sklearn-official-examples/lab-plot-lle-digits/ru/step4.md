# Построение результатов

Мы построим полученную проекцию, заданную каждым методом.

```python
for name in timing:
    title = f"{name} (time {timing[name]:.3f}s)"
    plot_embedding(projections[name], title)

plt.show()
```
