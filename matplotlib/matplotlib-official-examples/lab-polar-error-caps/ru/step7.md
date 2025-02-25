# Создаем большие погрешностные полосы по радиусу

В этом шаге мы создадим большие погрешностные полосы по радиусу, чтобы показать, как они могут привести к нежелательному масштабу в данных, уменьшая диапазон отображения.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=0.25, yerr=10.1, capsize=7, fmt="o", c="orangered")
ax.set_title("Large Radius Error Bars")
plt.show()
```
