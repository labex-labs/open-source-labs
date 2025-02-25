# Définir la fonction d'événement de pression de touches

Ensuite, nous définissons une fonction `on_press` qui sera appelée lorsqu'une touche est pressée. Cette fonction prend un paramètre `event` qui contient des informations sur la touche qui a été pressée. Dans cet exemple, nous allons basculer la visibilité de l'étiquette x lorsque la touche 'x' est pressée.

```python
def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
```
