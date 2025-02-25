# Скрываем верхнюю и правую оси

Теперь скрываем верхнюю и правую оси, так как нам нужны только левая и нижняя оси.

```python
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
```
