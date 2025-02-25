# Построим что-то на подграфиках

Мы построим что-то на подграфиках, чтобы пользователь мог увидеть эффект работы RectangleSelector и EllipseSelector.

```python
N = 100000  # Если N велико, можно увидеть улучшение при использовании blitting.
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # построим что-то
```
