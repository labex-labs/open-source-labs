# Création d'une fonction de test de frappe personnalisée

Dans cette étape, nous allons définir un sélecteur personnalisé en configurant picker avec une fonction appelable. La fonction déterminera si l'artiste est touché par l'événement souris. Si l'événement souris se trouve au-dessus de l'artiste, nous renverrons hit=True et props est un dictionnaire de propriétés que vous souhaitez ajouter aux attributs `.PickEvent`.

```python
def line_picker(line, mouseevent):
    """
    Trouvez les points à une certaine distance du clic de souris dans
    les coordonnées de données et attachez quelques attributs supplémentaires, pickx et picky
    qui sont les points de données qui ont été sélectionnés.
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
ax.set_title('sélecteur personnalisé pour les données de ligne')
line, = ax.plot(rand(100), rand(100), 'o', picker=line_picker)
fig.canvas.mpl_connect('pick_event', onpick2)
```
