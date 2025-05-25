# Adicionar dados ao gráfico

Finalmente, você pode adicionar alguns dados ao gráfico para visualizá-lo. Neste caso, você pode usar a função `plot()` para plotar uma onda senoidal.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
