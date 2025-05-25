# Criando um Gráfico Básico

Para criar um gráfico básico, precisamos definir os valores de x e y e, em seguida, plotá-los usando `plt.plot()`. Aqui, plotaremos duas ondas senoidais.

```python
x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)

plt.plot(x, y1, label='sin(2pix)')
plt.plot(x, y2, label='sin(4pix)')
```
