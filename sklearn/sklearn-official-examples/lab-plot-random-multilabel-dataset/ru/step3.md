# Строим график датасета

Теперь мы строим случайно сгенерированный мультиметкажный датасет с использованием функции `plot_2d`. Создаем фигуру с двумя подграфиками и вызываем функцию `plot_2d` для каждого подграфика с разными значениями параметров.

```python
_, (ax1, ax2) = plt.subplots(1, 2, sharex="row", sharey="row", figsize=(8, 4))
plt.subplots_adjust(bottom=0.15)

p_c, p_w_c = plot_2d(ax1, n_labels=1)
ax1.set_title("n_labels=1, length=50")
ax1.set_ylabel("Feature 1 count")

plot_2d(ax2, n_labels=3)
ax2.set_title("n_labels=3, length=50")
ax2.set_xlim(left=0, auto=True)
ax2.set_ylim(bottom=0, auto=True)

plt.show()
```
