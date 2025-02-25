# Crear las funciones de devolución de llamada de los botones

Ahora, crearemos dos funciones de devolución de llamada para los botones `Siguiente` y `Anterior`. Estas funciones actualizarán la trama con una nueva onda senoidal con una frecuencia diferente.

```python
class Index:
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
```
