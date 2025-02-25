# Definieren der Submit-Funktion

Wir definieren die `submit`-Funktion, die aufgerufen wird, wenn der Benutzer die Text-Eingabe abgibt. Diese Funktion aktualisiert die geplottete Funktion basierend auf der Benutzereingabe.

```python
def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
```
