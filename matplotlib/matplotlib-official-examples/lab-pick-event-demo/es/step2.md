# Creando una función de prueba de coincidencia personalizada

En este paso, definiremos un selector personalizado estableciendo picker en una función llamada. La función determinará si el artista es golpeado por el evento del mouse. Si el evento del mouse está sobre el artista, devolveremos hit=True y props es un diccionario de propiedades que desea agregar a los atributos de `.PickEvent`.

```python
def line_picker(line, mouseevent):
    """
    Encuentra los puntos a una cierta distancia del clic del mouse en
    coordenadas de datos y adjunta algunos atributos adicionales, pickx y picky
    que son los puntos de datos que se seleccionaron.
    """
    if mouseevent.xdata is None:
        return False, dict()
    xdata = line.get_xdata()
    ydata = line.get_ydata()
    maxd = 0.05
    d = np.sqrt(
        (xdata - mouseevent.xdata)**2 + (ydata - mouseevent.ydata)**2)

    ind, = np.nonzero(d <= maxd)
    if len(ind):
        pickx = xdata[ind]
        picky = ydata[ind]
        props = dict(ind=ind, pickx=pickx, picky=picky)
        return True, props
    else:
        return False, dict()


def onpick2(event):
    print('onpick2 line:', event.pickx, event.picky)


fig, ax = plt.subplots()
ax.set_title('custom picker for line data')
line, = ax.plot(rand(100), rand(100), 'o', picker=line_picker)
fig.canvas.mpl_connect('pick_event', onpick2)
```
