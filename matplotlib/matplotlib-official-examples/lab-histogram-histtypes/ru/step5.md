# Меняем стиль гистограммы

Мы можем изменить стиль гистограммы, указав параметр `histtype` в функции `hist`. В этом примере мы создадим гистограмму с ступенчатой кривой с заливкой цвета.

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```
