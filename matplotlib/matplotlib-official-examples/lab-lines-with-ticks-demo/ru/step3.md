# Построим кривую линию с эффектом делений

Теперь построим кривую линию с эффектом делений.

```python
# Plot a curved line with ticked style path
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```
