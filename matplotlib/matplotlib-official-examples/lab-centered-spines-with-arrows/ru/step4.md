# Скрытие ненужных осей координат (spines)

Вы также хотите скрыть верхнюю и правую оси координат (spines), так как они не нужны.

```python
ax.spines[["top", "right"]].set_visible(False)
```
