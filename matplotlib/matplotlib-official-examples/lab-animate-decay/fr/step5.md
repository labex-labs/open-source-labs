# Définir la fonction d'animation

Maintenant, nous devons définir la fonction qui mettra à jour le tracé pour chaque trame de l'animation. Cette fonction prendra les données générées par la fonction `data_gen()` et mettra à jour le tracé avec les nouvelles données. Nous mettrons également à jour les limites de l'axe des x au fur et à mesure que l'animation progresse.

```python
def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,
```
