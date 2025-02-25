# Выборочное заполнение горизонтальных областей

Параметр _where_ позволяет указать диапазоны x для заполнения. Это булевый массив того же размера, что и _x_. Только диапазоны x последовательностей из последовательных значений _True_ заполняются. Таким образом, область между соседними значениями _True_ и _False_ никогда не заполняется. Поэтому рекомендуется установить `interpolate=True`, если расстояние между точками данных по оси x не слишком велико, чтобы вышеописанный эффект был заметен.

```python
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                 interpolate=True)
fig.tight_layout()
```
