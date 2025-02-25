# Построение всех погрешностных полос

Далее мы построим все погрешностные полосы с использованием функции `errorbar` без какой - либо выборочной подвыборки. Это будет нашим базовым графиком.

```python
fig, ax = plt.subplots()

ax.set_title('All Errorbars')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, label='y2')

ax.legend()
plt.show()
```
