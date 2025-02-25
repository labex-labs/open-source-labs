# Crear una gráfica de ejemplo

Vamos a crear una gráfica de ejemplo para ver cómo se ve con las etiquetas de marcas del eje y en el lado derecho.

```python
x = np.arange(10)

fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax0.plot(x)
ax0.yaxis.tick_left()

ax1.plot(x)

plt.show()
```
