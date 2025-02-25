# Добавляем верхние пределы

Для добавления верхних пределов к стрелкам ошибки мы будем использовать параметр `uplims` функции `errorbar`. Мы также добавим постоянное значение 0,5 к значениям y, чтобы отличить этот график от предыдущего.

```python
# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```
