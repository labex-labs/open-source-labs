# Crear el gráfico

Ahora, podemos crear nuestro gráfico. Generaremos algunos datos utilizando NumPy y graficaremos una curva de decaimiento exponencial amortiguado.

```python
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')
```
