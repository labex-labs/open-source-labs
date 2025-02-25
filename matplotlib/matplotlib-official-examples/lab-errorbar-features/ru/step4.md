# Построение графика с переменными симметричными линейками ошибок

Теперь построим наши данные с переменными симметричными линейками ошибок. Функция `ax.errorbar()` используется для создания графика, а параметр `yerr` используется для указания значений ошибок.

```python
# plot variable, symmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='-o')
ax.set_title('Variable, Symmetric Error Bars')
plt.show()
```
