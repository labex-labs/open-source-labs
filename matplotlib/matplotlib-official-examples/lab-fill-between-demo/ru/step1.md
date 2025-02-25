# Основное использование

Функция `fill_between` может быть использована для заполнения области между двумя линиями. Параметры _y1_ и _y2_ могут быть скалярами, что означает горизонтальную границу при заданных значениях y. Если задан только _y1_, то _y2_ по умолчанию равен 0.

```python
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(6, 6))

ax1.fill_between(x, y1)
ax1.set_title('fill between y1 and 0')

ax2.fill_between(x, y1, 1)
ax2.set_title('fill between y1 and 1')

ax3.fill_between(x, y1, y2)
ax3.set_title('fill between y1 and y2')
ax3.set_xlabel('x')
fig.tight_layout()
```
