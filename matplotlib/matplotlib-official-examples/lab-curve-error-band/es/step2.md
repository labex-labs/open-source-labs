# Definir la curva

A continuación, definimos la curva alrededor de la cual queremos dibujar la banda de error. En este ejemplo, utilizaremos una curva paramétrica. Una curva paramétrica x(t), y(t) se puede dibujar directamente utilizando `~.Axes.plot`.

```python
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
```
