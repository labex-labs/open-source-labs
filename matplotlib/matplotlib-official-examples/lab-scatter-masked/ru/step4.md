# Добавление линии для отделения замаскированных областей

Наконец, мы добавляем линию, чтобы отделить замаскированные области. Мы создаем массив значений theta и рисуем круг с радиусом `r0` с использованием `np.cos(theta)` и `np.sin(theta)`.

```python
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```
