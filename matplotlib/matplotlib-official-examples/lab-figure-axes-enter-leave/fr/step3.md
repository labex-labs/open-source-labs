# Définition des gestionnaires d'événements

Nous allons maintenant définir quatre fonctions de gestionnaire d'événements : `on_enter_axes`, `on_leave_axes`, `on_enter_figure` et `on_leave_figure`. Ces fonctions seront appelées lorsque la souris entre ou sort d'un axe ou de la figure.

```python
def on_enter_axes(event):
    print('enter_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()

def on_leave_axes(event):
    print('leave_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()

def on_enter_figure(event):
    print('enter_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('red')
    event.canvas.draw()

def on_leave_figure(event):
    print('leave_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('grey')
    event.canvas.draw()
```
