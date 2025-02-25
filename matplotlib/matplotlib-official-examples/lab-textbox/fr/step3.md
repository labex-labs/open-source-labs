# Définir la fonction de soumission

Nous définissons la fonction `submit` qui sera appelée lorsque l'utilisateur soumettra l'entrée de texte. Cette fonction met à jour la fonction tracée en fonction de l'entrée de l'utilisateur.

```python
def submit(expression):
    """
    Met à jour la fonction tracée avec la nouvelle expression mathématique *expression*.

    *expression* est une chaîne de caractères utilisant "t" comme variable indépendante, par exemple
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
```
