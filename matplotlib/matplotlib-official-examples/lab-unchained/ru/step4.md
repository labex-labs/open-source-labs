# Настройка пределов и удаление делений на осях

В этом шаге мы установим пределы по оси y и удалим деления на графике.

```python
# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])
```
