# Добавление текстового поля на график

Наконец, мы добавим текстовое поле на график с использованием `matplotlib.pyplot.text()`. Мы укажем расположение текстового поля в координатах осей и используем параметр `bbox` для добавления свойств рамки.

```python
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
```
