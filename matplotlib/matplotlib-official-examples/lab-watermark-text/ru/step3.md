# Добавляем текстовую водяную знак

Для добавления текстовой водяной знаки мы можем использовать метод `text()` объекта `Figure`. Нам нужно указать позицию, текст и другие свойства, такие как размер шрифта, цвет и прозрачность.

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```
