# Définissez la fonction de rappel de sélection

La fonction de rappel de sélection sera appelée chaque fois que l'utilisateur sélectionne un rectangle ou une ellipse. La fonction recevra les événements de clic et de relâchement en tant qu'arguments et affichera les coordonnées du rectangle ou de l'ellipse.

```python
def select_callback(eclick, erelease):
    """
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f"The buttons you used were: {eclick.button} {erelease.button}")
```
