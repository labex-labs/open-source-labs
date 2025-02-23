# Добавляем текстовые аннотации на график

Далее мы добавим текстовые аннотации на график с использованием функции `ax.text()`. Создадим две аннотации, одну для "Sample A" и другую для "Sample B".

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)
```
