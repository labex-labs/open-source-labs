# Définir la fonction d'initialisation

Nous devons définir une fonction d'initialisation qui définira l'état initial du tracé. Dans cette fonction, nous définirons les limites de l'axe des y et effacerons les données de l'objet de ligne.

```python
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,
```
