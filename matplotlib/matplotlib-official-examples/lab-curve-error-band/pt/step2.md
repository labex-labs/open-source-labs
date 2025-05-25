# Definir a Curva

Em seguida, definimos a curva em torno da qual queremos desenhar a faixa de erro. Neste exemplo, usaremos uma curva parametrizada. Uma curva parametrizada x(t), y(t) pode ser desenhada diretamente usando `~.Axes.plot`.

```python
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
```
