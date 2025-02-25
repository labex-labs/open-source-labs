# Animar el gráfico

El quinto paso es animar el gráfico. Utilizaremos un bucle `for` para iterar a través de una serie de valores para phi. En cada iteración, eliminaremos la colección de líneas anterior, generaremos nuevos datos, graficaremos el nuevo wireframe y pausaremos brevemente antes de continuar.

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```
