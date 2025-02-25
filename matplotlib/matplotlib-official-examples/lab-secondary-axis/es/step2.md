# Trazar los datos

Crearemos una simple onda senoidal para demostrar el uso de un eje secundario. Trazaremos la onda senoidal utilizando grados como el eje x.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('ángulo [grados]')
ax.set_ylabel('señal')
ax.set_title('Onda senoidal')
```
