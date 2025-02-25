# Создаем перекрывающиеся погрешностные полосы по значению theta

В этом шаге мы создадим перекрывающиеся погрешностные полосы по значению theta, чтобы показать, как они могут ухудшить читаемость получаемого графика.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=5.25, yerr=0.1, capsize=7, fmt="o", c="darkred")
ax.set_title("Overlapping Theta Error Bars")
plt.show()
```
