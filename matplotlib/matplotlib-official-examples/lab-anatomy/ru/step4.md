# Добавим метки и заголовок

Теперь мы добавим метки к осям x и y, а также заголовок к рисунку с использованием методов `set_xlabel()`, `set_ylabel()` и `set_title()`.

```python
# Add labels and title
ax.set_xlabel("x Axis label", fontsize=14)
ax.set_ylabel("y Axis label", fontsize=14)
ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
```
