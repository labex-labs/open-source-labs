# Добавляем нижние пределы

Для добавления нижних пределов к стрелкам ошибки мы будем использовать параметр `lolims` функции `errorbar`. Мы также добавим постоянное значение 1,0 к значениям y, чтобы отличить этот график от предыдущих.

```python
# including lower limits
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```
