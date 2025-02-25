# Построение графика с переменными асимметричными линейками ошибок

Далее построим наши данные с переменными асимметричными линейками ошибок. Опять используется функция `ax.errorbar()`, но на этот раз параметр `xerr` используется для указания значений асимметричных ошибок.

```python
# plot variable, asymmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax.set_title('Variable, Asymmetric Error Bars')
plt.show()
```
