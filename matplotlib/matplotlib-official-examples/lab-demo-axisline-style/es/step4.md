# Graficar la gráfica

Ahora graficaremos la gráfica utilizando `np.linspace` y `np.sin`.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
