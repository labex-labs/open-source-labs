# Построение графика с логарифмической шкалой и линейками ошибок

Наконец, построим наши данные с логарифмической шкалой и линейками ошибок. Функция `ax.set_yscale()` используется для настройки оси y на логарифмическую шкалу.

```python
# plot log scale with error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='o')
ax.set_title('Log Scale with Error Bars')
ax.set_yscale('log')
plt.show()
```
