# Добавляем верхние и нижние пределы

Для добавления как верхних, так и нижних пределов к стрелкам ошибки мы будем использовать параметры `uplims` и `lolims` функции `errorbar`. Мы также добавим маркер на график, чтобы отличить его от предыдущих.

```python
# including upper and lower limits
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```
