# Создаем синусоидальные линии

Мы создадим синусоидальные линии с цветами из стандартного цикла цветов.

```python
# Create sinusoidal lines
L = 2*np.pi
x = np.linspace(0, L)
ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

for s in shift:
    plt.plot(x, np.sin(x + s), '-')
plt.margins(0)
plt.show()
```
