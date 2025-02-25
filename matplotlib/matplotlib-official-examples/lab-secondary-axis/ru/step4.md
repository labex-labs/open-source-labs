# Построим еще один пример

Теперь построим еще один пример преобразования от волнового числа к длине волны в логарифмическом масштабе. Для этого примера будем использовать случайный спектр.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Random spectrum')
```
