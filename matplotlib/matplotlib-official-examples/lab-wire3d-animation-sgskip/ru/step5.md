# Анимировать график

Пятым шагом является анимация графика. Мы будем использовать цикл for для перебора диапазона значений для phi. В каждой итерации мы удалим предыдущую коллекцию линий, сгенерируем новые данные, построим новый виртуальный фрейм (wireframe) и поставим короткую паузу перед продолжением.

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```
