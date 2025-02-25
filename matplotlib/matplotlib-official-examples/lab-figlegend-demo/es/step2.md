# Creando un gráfico básico

Para crear un gráfico básico, necesitamos definir los valores de x e y y luego representarlos utilizando `plt.plot()`. Aquí, representaremos dos ondas senoidales.

```python
x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)

plt.plot(x, y1, label='sin(2pix)')
plt.plot(x, y2, label='sin(4pix)')
```
