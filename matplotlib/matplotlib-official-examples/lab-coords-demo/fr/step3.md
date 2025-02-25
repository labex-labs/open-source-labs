# Événement de clic de souris

Nous pouvons nous connecter à des événements de clic de souris en utilisant la méthode `button_press_event`. Dans cet exemple, nous déconnectons la fonction de rappel d'événement de mouvement de souris lorsque le bouton gauche de la souris est cliqué.

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```
