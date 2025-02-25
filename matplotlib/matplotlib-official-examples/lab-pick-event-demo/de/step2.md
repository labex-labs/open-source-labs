# Erstellen einer benutzerdefinierten Trefferprüfungsfunktion

In diesem Schritt werden wir einen benutzerdefinierten Auswähler definieren, indem wir "picker" auf eine aufrufbare Funktion setzen. Die Funktion wird bestimmen, ob der Künstler vom Mausereignis getroffen wird. Wenn das Mausereignis über dem Künstler liegt, geben wir hit=True zurück und props ist ein Wörterbuch von Eigenschaften, die Sie zu den `.PickEvent`-Attributen hinzufügen möchten.

```python
def line_picker(line, mouseevent):
    """
    Finden Sie die Punkte innerhalb einer bestimmten Entfernung vom Mausklick in
    Datenkoordinaten und fügen Sie einige zusätzliche Attribute hinzu, pickx und picky
    die die ausgewählten Datenpunkte sind.
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
