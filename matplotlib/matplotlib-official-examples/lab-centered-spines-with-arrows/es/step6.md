# Agregar datos a la gráfica

Finalmente, se pueden agregar algunos datos a la gráfica para visualizarlos. En este caso, se puede utilizar la función `plot()` para trazar una onda sinusoidal.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
